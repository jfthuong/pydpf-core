
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples\06-distributed-post\01-distributed_delegate_to_server.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_06-distributed-post_01-distributed_delegate_to_server.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_06-distributed-post_01-distributed_delegate_to_server.py:


.. _ref_distributed_delegate_to_server:

Compute total displacement from distributed files with distributed post
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This example shows how distributed files can be read and post processed
on distributed processes. After remote post processing of total displacement,
results a merged on the local process. In this example, the client is only
connected to the coordinator server. Connections to remote processes are only
done implicitly through the coordinator.

.. GENERATED FROM PYTHON SOURCE LINES 15-16

Import dpf module and its examples files

.. GENERATED FROM PYTHON SOURCE LINES 16-21

.. code-block:: default


    from ansys.dpf import core as dpf
    from ansys.dpf.core import examples
    from ansys.dpf.core import operators as ops








.. GENERATED FROM PYTHON SOURCE LINES 22-24

Create the template workflow of total displacement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 24-29

.. code-block:: default


    template_workflow = dpf.Workflow()
    displacement = ops.result.displacement()
    norm = ops.math.norm_fc(displacement)








.. GENERATED FROM PYTHON SOURCE LINES 30-32

Add the operators to the template workflow and name its inputs and outputs
Once workflow's inputs and outputs are named, they can be connected later on

.. GENERATED FROM PYTHON SOURCE LINES 32-36

.. code-block:: default

    template_workflow.add_operators([displacement, norm])
    template_workflow.set_input_name("data_sources", displacement.inputs.data_sources)
    template_workflow.set_output_name("out", norm.outputs.fields_container)








.. GENERATED FROM PYTHON SOURCE LINES 37-50

Configure the servers
~~~~~~~~~~~~~~~~~~~~~~
Make a list of ip addresses an port numbers on which dpf servers are
started. Workflows instances will be created on each of those servers to
address each a different result file.
In this example, we will post process an analysis distributed in 2 files,
we will consequently require 2 remote processes
To make this example easier, we will start local servers here,
but we could get connected to any existing servers on the network.
We only keep instances of remote_servers to start and keep those servers
awaik. The purpose of this example is to show that we can do distributed
post processing without opening channels between this client and
the remote processes

.. GENERATED FROM PYTHON SOURCE LINES 50-55

.. code-block:: default


    remote_servers = [dpf.start_local_server(as_global=False), dpf.start_local_server(as_global=False)]
    ips = [remote_server.ip for remote_server in remote_servers]
    ports = [remote_server.port for remote_server in remote_servers]








.. GENERATED FROM PYTHON SOURCE LINES 56-57

Print the ips and ports

.. GENERATED FROM PYTHON SOURCE LINES 57-60

.. code-block:: default

    print("ips:", ips)
    print("ports:", ports)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    ips: ['127.0.0.1', '127.0.0.1']
    ports: [50057, 50058]




.. GENERATED FROM PYTHON SOURCE LINES 61-63

Here we show how we could send files in temporary directory if we were not
in shared memory

.. GENERATED FROM PYTHON SOURCE LINES 63-67

.. code-block:: default

    files = examples.download_distributed_files()
    server_file_paths = [dpf.upload_file_in_tmp_folder(files[0], server=remote_servers[0]),
                         dpf.upload_file_in_tmp_folder(files[1], server=remote_servers[1])]








.. GENERATED FROM PYTHON SOURCE LINES 68-72

Send workflows on servers
~~~~~~~~~~~~~~~~~~~~~~~~~~
Here we create new instances on the server by copies of the template workflow
We also connect the data sources to those workflows.

.. GENERATED FROM PYTHON SOURCE LINES 72-78

.. code-block:: default

    remote_workflows = []
    for i, ip in enumerate(ips):
        remote_workflows.append(template_workflow.create_on_other_server(ip=ip, port=ports[i]))
        ds = dpf.DataSources(server_file_paths[i])
        remote_workflows[i].connect("data_sources", ds)








.. GENERATED FROM PYTHON SOURCE LINES 79-81

Create a local workflow able to merge the results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 81-89

.. code-block:: default


    local_workflow = dpf.Workflow()
    merge = ops.utility.merge_fields_containers()
    local_workflow.add_operator(merge)
    local_workflow.set_input_name("in0", merge, 0)
    local_workflow.set_input_name("in1", merge, 1)
    local_workflow.set_output_name("merged", merge.outputs.merged_fields_container)








.. GENERATED FROM PYTHON SOURCE LINES 90-92

Connect the workflows together and get the output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. GENERATED FROM PYTHON SOURCE LINES 92-102

.. code-block:: default


    for i, ip in enumerate(ips):
        local_workflow.connect_with(remote_workflows[i], ("out", "in" + str(i)))

    fc = local_workflow.get_output("merged", dpf.types.fields_container)
    print(fc)
    print(fc[0].min().data)
    print(fc[0].max().data)

    dpf.server.shutdown_all_session_servers()




.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    DPF  Fields Container
      with 1 field(s)
      defined on labels: time 

      with:
      - field 0 {time:  1} with Nodal location, 1 components and 432 entities.

    [0.]
    [10.03242272]
    ("'NoneType' object has no attribute 'shutdown'",)





.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.913 seconds)


.. _sphx_glr_download_examples_06-distributed-post_01-distributed_delegate_to_server.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: 01-distributed_delegate_to_server.py <01-distributed_delegate_to_server.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: 01-distributed_delegate_to_server.ipynb <01-distributed_delegate_to_server.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
