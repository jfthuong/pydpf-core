"""
included_fields
===============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "logic" category
"""

class included_fields(Operator):
    """Check if one field belongs to another.

      available inputs:
        - fieldA (Field)
        - fieldB (Field)
        - double_value (float)
        - double_tolerance (float) (optional)

      available outputs:
        - included (bool)
        - message (str)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.logic.included_fields()

      >>> # Make input connections
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_double_value = float()
      >>> op.inputs.double_value.connect(my_double_value)
      >>> my_double_tolerance = float()
      >>> op.inputs.double_tolerance.connect(my_double_tolerance)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.logic.included_fields(fieldA=my_fieldA,fieldB=my_fieldB,double_value=my_double_value,double_tolerance=my_double_tolerance)

      >>> # Get output data
      >>> result_included = op.outputs.included()
      >>> result_message = op.outputs.message()"""
    def __init__(self, fieldA=None, fieldB=None, double_value=None, double_tolerance=None, config=None, server=None):
        super().__init__(name="Are_fields_included", config = config, server = server)
        self._inputs = InputsIncludedFields(self)
        self._outputs = OutputsIncludedFields(self)
        if fieldA !=None:
            self.inputs.fieldA.connect(fieldA)
        if fieldB !=None:
            self.inputs.fieldB.connect(fieldB)
        if double_value !=None:
            self.inputs.double_value.connect(double_value)
        if double_tolerance !=None:
            self.inputs.double_tolerance.connect(double_tolerance)

    @staticmethod
    def _spec():
        spec = Specification(description="""Check if one field belongs to another.""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "fieldA", type_names=["field"], optional=False, document=""""""), 
                                 1 : PinSpecification(name = "fieldB", type_names=["field"], optional=False, document=""""""), 
                                 2 : PinSpecification(name = "double_value", type_names=["double"], optional=False, document="""Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14)."""), 
                                 3 : PinSpecification(name = "double_tolerance", type_names=["double"], optional=True, document="""Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "included", type_names=["bool"], optional=False, document="""bool (true if belongs...)"""), 
                                 1 : PinSpecification(name = "message", type_names=["string"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "Are_fields_included")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsIncludedFields 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsIncludedFields 
        """
        return super().outputs


#internal name: Are_fields_included
#scripting name: included_fields
class InputsIncludedFields(_Inputs):
    """Intermediate class used to connect user inputs to included_fields operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.included_fields()
      >>> my_fieldA = dpf.Field()
      >>> op.inputs.fieldA.connect(my_fieldA)
      >>> my_fieldB = dpf.Field()
      >>> op.inputs.fieldB.connect(my_fieldB)
      >>> my_double_value = float()
      >>> op.inputs.double_value.connect(my_double_value)
      >>> my_double_tolerance = float()
      >>> op.inputs.double_tolerance.connect(my_double_tolerance)
    """
    def __init__(self, op: Operator):
        super().__init__(included_fields._spec().inputs, op)
        self._fieldA = Input(included_fields._spec().input_pin(0), 0, op, -1) 
        self._inputs.append(self._fieldA)
        self._fieldB = Input(included_fields._spec().input_pin(1), 1, op, -1) 
        self._inputs.append(self._fieldB)
        self._double_value = Input(included_fields._spec().input_pin(2), 2, op, -1) 
        self._inputs.append(self._double_value)
        self._double_tolerance = Input(included_fields._spec().input_pin(3), 3, op, -1) 
        self._inputs.append(self._double_tolerance)

    @property
    def fieldA(self):
        """Allows to connect fieldA input to the operator

        Parameters
        ----------
        my_fieldA : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.included_fields()
        >>> op.inputs.fieldA.connect(my_fieldA)
        >>> #or
        >>> op.inputs.fieldA(my_fieldA)

        """
        return self._fieldA

    @property
    def fieldB(self):
        """Allows to connect fieldB input to the operator

        Parameters
        ----------
        my_fieldB : Field, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.included_fields()
        >>> op.inputs.fieldB.connect(my_fieldB)
        >>> #or
        >>> op.inputs.fieldB(my_fieldB)

        """
        return self._fieldB

    @property
    def double_value(self):
        """Allows to connect double_value input to the operator

        - pindoc: Double positive small value. Smallest value which will be considered during the comparison step: all the abs(values) in field less than this value is considered as null, (default value:1.0e-14).

        Parameters
        ----------
        my_double_value : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.included_fields()
        >>> op.inputs.double_value.connect(my_double_value)
        >>> #or
        >>> op.inputs.double_value(my_double_value)

        """
        return self._double_value

    @property
    def double_tolerance(self):
        """Allows to connect double_tolerance input to the operator

        - pindoc: Double relative tolerance. Maximum tolerance gap between to compared values: values within relative tolerance are considered identical (v1-v2)/v2 < relativeTol (default is 0.001).

        Parameters
        ----------
        my_double_tolerance : float, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.included_fields()
        >>> op.inputs.double_tolerance.connect(my_double_tolerance)
        >>> #or
        >>> op.inputs.double_tolerance(my_double_tolerance)

        """
        return self._double_tolerance

class OutputsIncludedFields(_Outputs):
    """Intermediate class used to get outputs from included_fields operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.logic.included_fields()
      >>> # Connect inputs : op.inputs. ...
      >>> result_included = op.outputs.included()
      >>> result_message = op.outputs.message()
    """
    def __init__(self, op: Operator):
        super().__init__(included_fields._spec().outputs, op)
        self._included = Output(included_fields._spec().output_pin(0), 0, op) 
        self._outputs.append(self._included)
        self._message = Output(included_fields._spec().output_pin(1), 1, op) 
        self._outputs.append(self._message)

    @property
    def included(self):
        """Allows to get included output of the operator


        - pindoc: bool (true if belongs...)

        Returns
        ----------
        my_included : bool, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.included_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_included = op.outputs.included() 
        """
        return self._included

    @property
    def message(self):
        """Allows to get message output of the operator


        Returns
        ----------
        my_message : str, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.logic.included_fields()
        >>> # Connect inputs : op.inputs. ...
        >>> result_message = op.outputs.message() 
        """
        return self._message
