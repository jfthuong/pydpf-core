"""
merge_supports
==============
"""
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs, _modify_output_spec_with_one_type
from ansys.dpf.core.operators.specification import PinSpecification, Specification

"""Operators from Ans.Dpf.Native plugin, from "utility" category
"""

class merge_supports(Operator):
    """Take a set of supports and assemble them in a unique one

      available inputs:
        - supports1 (AbstractFieldSupport)
        - supports2 (AbstractFieldSupport)

      available outputs:
        - merged_support (AbstractFieldSupport)

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> # Instantiate operator
      >>> op = dpf.operators.utility.merge_supports()

      >>> # Make input connections
      >>> my_supports1 = dpf.AbstractFieldSupport()
      >>> op.inputs.supports1.connect(my_supports1)
      >>> my_supports2 = dpf.AbstractFieldSupport()
      >>> op.inputs.supports2.connect(my_supports2)

      >>> # Instantiate operator and connect inputs in one line
      >>> op = dpf.operators.utility.merge_supports(supports1=my_supports1,supports2=my_supports2)

      >>> # Get output data
      >>> result_merged_support = op.outputs.merged_support()"""
    def __init__(self, supports1=None, supports2=None, config=None, server=None):
        super().__init__(name="merge::abstract_support", config = config, server = server)
        self._inputs = InputsMergeSupports(self)
        self._outputs = OutputsMergeSupports(self)
        if supports1 !=None:
            self.inputs.supports1.connect(supports1)
        if supports2 !=None:
            self.inputs.supports2.connect(supports2)

    @staticmethod
    def _spec():
        spec = Specification(description="""Take a set of supports and assemble them in a unique one""",
                             map_input_pin_spec={
                                 0 : PinSpecification(name = "supports", type_names=["abstract_field_support"], optional=False, document="""A vector of supports to merge or supports from pin 0 to ..."""), 
                                 1 : PinSpecification(name = "supports", type_names=["abstract_field_support"], optional=False, document="""A vector of supports to merge or supports from pin 0 to ...""")},
                             map_output_pin_spec={
                                 0 : PinSpecification(name = "merged_support", type_names=["abstract_field_support"], optional=False, document="""""")})
        return spec


    @staticmethod
    def default_config():
        return Operator.default_config(name = "merge::abstract_support")

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsMergeSupports 
        """
        return super().inputs


    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsMergeSupports 
        """
        return super().outputs


#internal name: merge::abstract_support
#scripting name: merge_supports
class InputsMergeSupports(_Inputs):
    """Intermediate class used to connect user inputs to merge_supports operator

      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_supports()
      >>> my_supports1 = dpf.AbstractFieldSupport()
      >>> op.inputs.supports1.connect(my_supports1)
      >>> my_supports2 = dpf.AbstractFieldSupport()
      >>> op.inputs.supports2.connect(my_supports2)
    """
    def __init__(self, op: Operator):
        super().__init__(merge_supports._spec().inputs, op)
        self._supports1 = Input(merge_supports._spec().input_pin(0), 0, op, 0) 
        self._inputs.append(self._supports1)
        self._supports2 = Input(merge_supports._spec().input_pin(1), 1, op, 1) 
        self._inputs.append(self._supports2)

    @property
    def supports1(self):
        """Allows to connect supports1 input to the operator

        - pindoc: A vector of supports to merge or supports from pin 0 to ...

        Parameters
        ----------
        my_supports1 : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_supports()
        >>> op.inputs.supports1.connect(my_supports1)
        >>> #or
        >>> op.inputs.supports1(my_supports1)

        """
        return self._supports1

    @property
    def supports2(self):
        """Allows to connect supports2 input to the operator

        - pindoc: A vector of supports to merge or supports from pin 0 to ...

        Parameters
        ----------
        my_supports2 : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_supports()
        >>> op.inputs.supports2.connect(my_supports2)
        >>> #or
        >>> op.inputs.supports2(my_supports2)

        """
        return self._supports2

class OutputsMergeSupports(_Outputs):
    """Intermediate class used to get outputs from merge_supports operator
      Examples
      --------
      >>> from ansys.dpf import core as dpf

      >>> op = dpf.operators.utility.merge_supports()
      >>> # Connect inputs : op.inputs. ...
      >>> result_merged_support = op.outputs.merged_support()
    """
    def __init__(self, op: Operator):
        super().__init__(merge_supports._spec().outputs, op)
        self._merged_support = Output(merge_supports._spec().output_pin(0), 0, op) 
        self._outputs.append(self._merged_support)

    @property
    def merged_support(self):
        """Allows to get merged_support output of the operator


        Returns
        ----------
        my_merged_support : AbstractFieldSupport, 

        Examples
        --------
        >>> from ansys.dpf import core as dpf

        >>> op = dpf.operators.utility.merge_supports()
        >>> # Connect inputs : op.inputs. ...
        >>> result_merged_support = op.outputs.merged_support() 
        """
        return self._merged_support
