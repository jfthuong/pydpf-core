"""
on_property
===========
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "scoping" category
"""

class on_property(Operator):
    """Provides a scoping at a given location based on a given property name and a property number.

      available inputs:
        - requested_location (str)
        - property_name (str)
        - property_id (int)
        - streams_container (StreamsContainer) (optional)
        - data_sources (DataSources)
        - inclusive (int) (optional)

      available outputs:
        - mesh_scoping (Scoping)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.scoping.on_property()

      >>> # Make input connections
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)
      >>> my_property_id = int()
      >>> op.inputs.property_id.connect(my_property_id)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_inclusive = int()
      >>> op.inputs.inclusive.connect(my_inclusive)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.scoping.on_property(requested_location=my_requested_location,property_name=my_property_name,property_id=my_property_id,streams_container=my_streams_container,data_sources=my_data_sources,inclusive=my_inclusive)

      >>> # Get output data
      >>> result_mesh_scoping = op.outputs.mesh_scoping()"""
    def __init__(self, requested_location=None, property_name=None, property_id=None, streams_container=None, data_sources=None, inclusive=None, config=None, server=None):
        super().__init__(name="scoping_provider_by_prop", config = config, server = server)
        self._inputs = InputsOnProperty(self)
        self._outputs = OutputsOnProperty(self)
        if requested_location !=None:
            self.inputs.requested_location.connect(requested_location)
        if property_name !=None:
            self.inputs.property_name.connect(property_name)
        if property_id !=None:
            self.inputs.property_id.connect(property_id)
        if streams_container !=None:
            self.inputs.streams_container.connect(streams_container)
        if data_sources !=None:
            self.inputs.data_sources.connect(data_sources)
        if inclusive !=None:
            self.inputs.inclusive.connect(inclusive)

    @staticmethod
    def _spec():
        spec = Specification(description="""Provides a scoping at a given location based on a given property name and a property number.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "requested_location", type_names=["string"], optional=False, document="""Nodal or Elemental location are expected"""), 
                                 1 : PinSpecification(name = "property_name", type_names=["string"], optional=False, document="""ex "mapdl_element_type", "apdl_type_index", "mapdl_type_id", "material", "apdl_section_id", "apdl_real_id", "shell_axi", "volume_axi"..."""), 
                                 2 : PinSpecification(name = "property_id", type_names=["int32"], optional=False, document=""""""), 
                                 3 : PinSpecification(name = "streams_container", type_names=["streams_container"], optional=True, document=""""""), 
                                 4 : PinSpecification(name = "data_sources", type_names=["data_sources"], optional=False, document=""""""), 
                                 5 : PinSpecification(name = "inclusive", type_names=["int32"], optional=True, document="""If element scoping is requested on a nodal named selection, if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "mesh_scoping", type_names=["scoping"], optional=False, document="""Scoping""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "scoping_provider_by_prop")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsOnProperty 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsOnProperty 
        """
        return super().outputs


#internal name: scoping_provider_by_prop
#scripting name: on_property
class InputsOnProperty(_Inputs):
    """Intermediate class used to connect user inputs to on_property operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.on_property()
      >>> my_requested_location = str()
      >>> op.inputs.requested_location.connect(my_requested_location)
      >>> my_property_name = str()
      >>> op.inputs.property_name.connect(my_property_name)
      >>> my_property_id = int()
      >>> op.inputs.property_id.connect(my_property_id)
      >>> my_streams_container = dpf.StreamsContainer()
      >>> op.inputs.streams_container.connect(my_streams_container)
      >>> my_data_sources = dpf.DataSources()
      >>> op.inputs.data_sources.connect(my_data_sources)
      >>> my_inclusive = int()
      >>> op.inputs.inclusive.connect(my_inclusive)
    """
    def __init__(self, op: Operator):
        super().__init__(on_property._spec().inputs, op)
        self._requested_location = Input(on_property._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._requested_location)
        self._property_name = Input(on_property._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._property_name)
        self._property_id = Input(on_property._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._property_id)
        self._streams_container = Input(on_property._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._streams_container)
        self._data_sources = Input(on_property._spec().input_pin(4), 4, op, -1) 
        self._inputs.append(self._data_sources)
        self._inclusive = Input(on_property._spec().input_pin(5), 5, op, -1) 
        self._inputs.append(self._inclusive)

    @property
    def requested_location(self):
        """Allows to connect requested_location input to the operator

        - pindoc: Nodal or Elemental location are expected

        Parameters
        ----------
        my_requested_location : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_property()
        >>> op.inputs.requested_location.connect(my_requested_location)
        >>> #or
        >>> op.inputs.requested_location(my_requested_location)

        """
        return self._requested_location

    @property
    def property_name(self):
        """Allows to connect property_name input to the operator

        - pindoc: ex "mapdl_element_type", "apdl_type_index", "mapdl_type_id", "material", "apdl_section_id", "apdl_real_id", "shell_axi", "volume_axi"...

        Parameters
        ----------
        my_property_name : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_property()
        >>> op.inputs.property_name.connect(my_property_name)
        >>> #or
        >>> op.inputs.property_name(my_property_name)

        """
        return self._property_name

    @property
    def property_id(self):
        """Allows to connect property_id input to the operator

        Parameters
        ----------
        my_property_id : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_property()
        >>> op.inputs.property_id.connect(my_property_id)
        >>> #or
        >>> op.inputs.property_id(my_property_id)

        """
        return self._property_id

    @property
    def streams_container(self):
        """Allows to connect streams_container input to the operator

        Parameters
        ----------
        my_streams_container : StreamsContainer, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_property()
        >>> op.inputs.streams_container.connect(my_streams_container)
        >>> #or
        >>> op.inputs.streams_container(my_streams_container)

        """
        return self._streams_container

    @property
    def data_sources(self):
        """Allows to connect data_sources input to the operator

        Parameters
        ----------
        my_data_sources : DataSources, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_property()
        >>> op.inputs.data_sources.connect(my_data_sources)
        >>> #or
        >>> op.inputs.data_sources(my_data_sources)

        """
        return self._data_sources

    @property
    def inclusive(self):
        """Allows to connect inclusive input to the operator

        - pindoc: If element scoping is requested on a nodal named selection, if inclusive == 1 then all the elements adjacent to the nodes ids in input are added, if inclusive == 0, only the elements which have all their nodes in the scoping are included

        Parameters
        ----------
        my_inclusive : int, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_property()
        >>> op.inputs.inclusive.connect(my_inclusive)
        >>> #or
        >>> op.inputs.inclusive(my_inclusive)

        """
        return self._inclusive

class OutputsOnProperty(_Outputs):
    """Intermediate class used to get outputs from on_property operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.scoping.on_property()
      >>> # Connect inputs : op.inputs. ...
      >>> result_mesh_scoping = op.outputs.mesh_scoping()
    """
    def __init__(self, op: Operator):
        super().__init__(on_property._spec().outputs, op)
        self._mesh_scoping = Output(on_property._spec().output_pin(0), 0, op) 
        self._outputs.append(self._mesh_scoping)

    @property
    def mesh_scoping(self):
        """Allows to get mesh_scoping output of the operator


        - pindoc: Scoping

        Returns
        ----------
        my_mesh_scoping : Scoping, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.scoping.on_property()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh_scoping = op.outputs.mesh_scoping() 
        """
        return self._mesh_scoping
