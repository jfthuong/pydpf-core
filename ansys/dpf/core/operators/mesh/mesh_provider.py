"""
mesh_provider
=============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "mesh" category
"""

class mesh_provider(Operator):
    """Read a mesh from result files and cure degenerated elements

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)
        - read_cyclic (int) (optional)

      available outputs:
        - mesh (MeshedRegion)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.mesh.mesh_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_read_cyclic = int()
      >>> op.inputs.read_cyclic.connect(my_read_cyclic)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.mesh.mesh_provider(streams_container=my_streams_container,data_sources=my_data_sources)

      >>> # Get output data
      >>> result_mesh = op.outputs.mesh()"""
    def __init__(self, streams_container=None, data_sources=None, config=None, server=None):
        super().__init__(name="MeshProvider", config = config, server = server)
        self._inputs = InputsMeshProvider(self)
        self._outputs = OutputsMeshProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read a mesh from result files and cure degenerated elements""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""result file container allowed to be kept open to cache data"""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""result file path container, used if no streams are set"""), 
                                 14 : PinSpecification(name = "read_cyclic", type_names=["int32"], optional=True, document="""if 1 cyclic symmetry is ignored, if 2 cyclic expansion is done (default is 1)""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh", type_names=["abstract_meshed_region"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "MeshProvider")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMeshProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMeshProvider 
        """
        return super().outputs


#internal name: MeshProvider
#scripting name: mesh_provider
class InputsMeshProvider(_Inputs):
    """Intermediate class used to connect user inputs to mesh_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_provider()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_read_cyclic = int()
      >>> op.inputs.read_cyclic.connect(my_read_cyclic)
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_provider._spec().inputs, op)
        self._streams_container = Input(mesh_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(mesh_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._read_cyclic = Input(mesh_provider._spec().input_pin(14), 14, op, -1) 
        self._inputs.append(self._read_cyclic)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: result file container allowed to be kept open to cache data

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: result file path container, used if no streams are set

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def read_cyclic(self):
        """Allows to connect read_cyclic input to the operator

        - pindoc: if 1 cyclic symmetry is ignored, if 2 cyclic expansion is done (default is 1)

        Parameters
        ----------
        my_read_cyclic : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_provider()
        >>> op.inputs.read_cyclic.connect(my_read_cyclic)
        >>> #or
        >>> op.inputs.read_cyclic(my_read_cyclic)

        """
        return self._read_cyclic

class OutputsMeshProvider(_Outputs):
    """Intermediate class used to get outputs from mesh_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.mesh.mesh_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh = op.outputs.mesh()
    """
    def __init__(self, op: Operator):
        super().__init__(mesh_provider._spec().outputs, op)
        self._mesh = Output(mesh_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator


        Returns
        ----------
        my_mesh : MeshedRegion, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.mesh.mesh_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh() 
        """
        return self._mesh
