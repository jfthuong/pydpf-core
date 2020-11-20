##########################################################################
#                                                                        #
#          Copyright (C) 2020 ANSYS Inc.  All Rights Reserved            #
#                                                                        #
# This file contains proprietary software licensed from ANSYS Inc.       #
# This header must remain in any source code despite modifications or    #
# enhancements by any party.                                             #
#                                                                        #
##########################################################################
# Version: 1.0                                                           #
# Author(s): C.Bellot/R.Lagha                                            #
# contact(s): ramdane.lagha@ansys.com                                    #
##########################################################################
import os
import logging
import time

import grpc

from ansys import dpf
from ansys.grpc.dpf import base_pb2, base_pb2_grpc

LOG = logging.getLogger(__name__)
LOG.setLevel('DEBUG')


if 'DPF_CONFIGURATION' in os.environ:
    CONFIGURATION = os.environ['DPF_CONFIGURATION']
else:
    CONFIGURATION = 'release'


class BaseService():
    """Base service connection to dpf server.  Used to load operators.

    Parameters
    ----------
    channel : channel, optional
        Channel connected to the remote or local instance. Defaults to the global channel.
        
    timeout : float, optional
        Fails when a connection takes longer than ``timeout`` seconds
        to initialize.

    Examples
    --------
    Connect to an existing DPF server
    >>> from ansys import dpf
    >>> dpf.core.BaseService(grpc.insecure_channel('127.0.0.1:50054'))
    """

    def __init__(self, channel=None, load_operators=True, timeout=5):
        """Initialize base service"""
        
        if channel is None:
            channel = dpf.core._global_channel()     
        
        self._channel = channel  
        self._stub = self._connect(timeout)
        
        try:
            if load_operators:
                self._load_mapdl_operators()
                self._load_mesh_operators()
        except :
            print("not all plugins have been loaded")

    def _connect(self, timeout=5):
        """Connect to dpf service within a given timeout"""
        stub = base_pb2_grpc.BaseServiceStub(self._channel)

        # verify connected
        if timeout is not None:
            state = grpc.channel_ready_future(self._channel)
            tstart = time.time()
            while (time.time() - tstart) < timeout and not state._matured:
                time.sleep(0.01)

            if not state._matured:
                raise IOError(f'Unable to connect to DPF instance at {self._channel}')

        return stub

    def load_library(self, filename, name='', symbol="LoadOperators"):
        """Dynamically load an operators library for dpf.core.

        Parameters
        ----------
        filename : str
            Filename of the operator library.

        name : str, optional
            Library name.  Probably optional

        Examples
        --------
        Load the mapdl operators for linux
        >>> from ansys import dpf
        >>> base = dpf.core.BaseService()
        >>> base.load_library('libmapdlOperatorsCore.so', 'mapdl_operators')

        Load a new operators libary
        >>> base.load_library('someNewOperators.so', 'new_operators')

        """
        # verify filename exists if it's a full path (this will not
        # work for a remote session or a file local to the dpf server)
        if os.path.dirname(filename):
            if not os.path.isfile(filename):
                raise FileNotFoundError('Library "%s" not found"' % filename)

        request = base_pb2.PluginRequest()
        request.name = name
        request.dllPath = filename
        request.symbol = symbol
        try:
            self._stub.Load(request)
        except Exception as e:
            raise IOError('Unable to load library "%s".  Check ' % filename +
                          'for missing dependencies or file may not exist:\n%s'
                          % str(e))

    def _load_mapdl_operators(self):
        """Load the mapdl operators library"""
        if os.name == 'posix':
            self.load_library('libmapdlOperatorsCore.so', 'mapdl_operators')
        else:
            if CONFIGURATION == "release":
                self.load_library('mapdlOperatorsCore.dll', 'mapdl_operators')
            else:
                self.load_library('mapdlOperatorsCoreD.dll', 'mapdl_operators')

    def _load_mesh_operators(self):
        """Load the mesh operators library"""
        if os.name == 'posix':
            self.load_library('libmeshOperatorsCore.so', 'mesh_operators')
        else:
            if CONFIGURATION == "release":
                self.load_library('meshOperatorsCore.dll', 'mesh_operators')
            else :
                self.load_library('meshOperatorsCoreD.dll', 'mesh_operators')