"""
cyclic_support_provider
=======================
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from mapdlOperatorsCore plugin, from "metadata" category
"""

class cyclic_support_provider(Operator):
    """Read the cyclic support (DPF entity containing necessary informations for expansions) and expands the mesh.

      available inputs:
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)
        - sector_meshed_region (MeshedRegion, MeshesContainer) (optional)
        - expanded_meshed_region (MeshedRegion, MeshesContainer) (optional)
        - sectors_to_expand (Scoping, ScopingsContainer, list) (optional)

      available outputs:
        - cyclic_support (CyclicSupport)
        - sector_meshes (MeshesContainer)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.metadata.cyclic_support_provider()

      >>> # Make input connections
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_sector_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
      >>> my_expanded_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)
      >>> my_sectors_to_expand = dpf.Scoping()
      >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.metadata.cyclic_support_provider(streams_container=my_streams_container,data_sources=my_data_sources,sector_meshed_region=my_sector_meshed_region,expanded_meshed_region=my_expanded_meshed_region,sectors_to_expand=my_sectors_to_expand)

      >>> # Get output data
      >>> result_cyclic_support = op.outputs.cyclic_support()
      >>> result_sector_meshes = op.outputs.sector_meshes()"""
    def __init__(self, streams_container=None, data_sources=None, sector_meshed_region=None, expanded_meshed_region=None, sectors_to_expand=None, config=None, server=None):
        super().__init__(name="mapdl::rst::support_provider_cyclic", config = config, server = server)
        self._inputs = InputsCyclicSupportProvider(self)
        self._outputs = OutputsCyclicSupportProvider(self)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if sector_meshed_region !=None:
            self.inputs.sector_meshed_region.connect(sector_meshed_region)
        if expanded_meshed_region !=None:
            self.inputs.expanded_meshed_region.connect(expanded_meshed_region)
        if sectors_to_expand !=None:
            self.inputs.sectors_to_expand.connect(sectors_to_expand)

    @staticmethod
    def _spec():
        spec = Specification(description="""Read the cyclic support (DPF entity containing necessary informations for expansions) and expands the mesh.""",
                             map_input_pin_spec={
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document="""Streams containing the result file."""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document="""data sources containing the result file."""), 
                                 7 : PinSpecification(name = "sector_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""mesh of the first sector."""), 
                                 15 : PinSpecification(name = "expanded_meshed_region", type_names=["abstract_meshed_region","meshes_container"], optional=True, document="""if this pin is set, expanding the mesh is not necessary."""), 
                                 18 : PinSpecification(name = "sectors_to_expand", type_names=["scoping","scopings_container","vector<int32>"], optional=True, document="""sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "cyclic_support", type_names=["cyclic_support"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "sector_meshes", type_names=["meshes_container"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "mapdl::rst::support_provider_cyclic")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsCyclicSupportProvider 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsCyclicSupportProvider 
        """
        return super().outputs


#internal name: mapdl::rst::support_provider_cyclic
#scripting name: cyclic_support_provider
class InputsCyclicSupportProvider(_Inputs):
    """Intermediate class used to connect user inputs to cyclic_support_provider operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.cyclic_support_provider()
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_sector_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
      >>> my_expanded_meshed_region = dpf.MeshedRegion()
      >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)
      >>> my_sectors_to_expand = dpf.Scoping()
      >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
    """
    def __init__(self, op: Operator):
        super().__init__(cyclic_support_provider._spec().inputs, op)
        self._streams_container = Input(cyclic_support_provider._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(cyclic_support_provider._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._sector_meshed_region = Input(cyclic_support_provider._spec().input_pin(7), 7, op, -1) 
        self._inputs.append(self._sector_meshed_region)
        self._expanded_meshed_region = Input(cyclic_support_provider._spec().input_pin(15), 15, op, -1) 
        self._inputs.append(self._expanded_meshed_region)
        self._sectors_to_expand = Input(cyclic_support_provider._spec().input_pin(18), 18, op, -1) 
        self._inputs.append(self._sectors_to_expand)

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        - pindoc: Streams containing the result file.

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_support_provider()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        - pindoc: data sources containing the result file.

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_support_provider()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def sector_meshed_region(self):
        """Allows to connect sector_meshed_region input to the operator

        - pindoc: mesh of the first sector.

        Parameters
        ----------
        my_sector_meshed_region : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_support_provider()
        >>> op.inputs.sector_meshed_region.connect(my_sector_meshed_region)
        >>> #or
        >>> op.inputs.sector_meshed_region(my_sector_meshed_region)

        """
        return self._sector_meshed_region

    @property
    def expanded_meshed_region(self):
        """Allows to connect expanded_meshed_region input to the operator

        - pindoc: if this pin is set, expanding the mesh is not necessary.

        Parameters
        ----------
        my_expanded_meshed_region : MeshedRegion, MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_support_provider()
        >>> op.inputs.expanded_meshed_region.connect(my_expanded_meshed_region)
        >>> #or
        >>> op.inputs.expanded_meshed_region(my_expanded_meshed_region)

        """
        return self._expanded_meshed_region

    @property
    def sectors_to_expand(self):
        """Allows to connect sectors_to_expand input to the operator

        - pindoc: sectors to expand (start at 0), for multistage: use scopings container with 'stage' label.

        Parameters
        ----------
        my_sectors_to_expand : Scoping, ScopingsContainer, list, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_support_provider()
        >>> op.inputs.sectors_to_expand.connect(my_sectors_to_expand)
        >>> #or
        >>> op.inputs.sectors_to_expand(my_sectors_to_expand)

        """
        return self._sectors_to_expand

class OutputsCyclicSupportProvider(_Outputs):
    """Intermediate class used to get outputs from cyclic_support_provider operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.metadata.cyclic_support_provider()
      >>> # Connect inputs : op.inputs. ...
      >>> result_cyclic_support = op.outputs.cyclic_support()
      >>> result_sector_meshes = op.outputs.sector_meshes()
    """
    def __init__(self, op: Operator):
        super().__init__(cyclic_support_provider._spec().outputs, op)
        self._cyclic_support = Output(cyclic_support_provider._spec().output_pin(0), 0, op) 
        self._outputs.append(self._cyclic_support)
        self._sector_meshes = Output(cyclic_support_provider._spec().output_pin(1), 1, op) 
        self._outputs.append(self._sector_meshes)

    @property
    def cyclic_support(self):
        """Allows to get cyclic_support output of the operator


        Returns
        ----------
        my_cyclic_support : CyclicSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_support_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_cyclic_support = op.outputs.cyclic_support() 
        """
        return self._cyclic_support

    @property
    def sector_meshes(self):
        """Allows to get sector_meshes output of the operator


        Returns
        ----------
        my_sector_meshes : MeshesContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.metadata.cyclic_support_provider()
        >>> # Connect inputs : op.inputs. ...
        >>> result_sector_meshes = op.outputs.sector_meshes() 
        """
        return self._sector_meshes
