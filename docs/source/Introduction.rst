
Introduction
===============

``findCPcli`` is a command line python-tool for the computation of chokepoint reactions in genome-scale metabolic models. 
The main purpose is to provide a tool to compute the chokepoints of the topology of the metabolic network, as well as considering also the dynamic information of the network.

findCPcli takes as inputs SBML files of genome-scale models and  provides as output spreadsheet files with the results of the chokepoint computation. 

Chokepoint reactions 
~~~~~~~~~~~~~~~~~~~~
Chokepoint reactions are those reactions that are either the unique consumer of a given metabolite or the only producer of a metabolite. 

Dead-End Metabolites (DEM) 
~~~~~~~~~~~~~~~~~~~~~~~~~~
Dead-End Metabolites (DEM) are those metabolites that are not produced or consumed by any reaction.

Example 
~~~~~~~
Chokepoint reactions and dead-end metabolites example:

.. image:: _static/chokepoints_example.png
    :align: center
    :alt: alternate text

The computation of chokepoints can also be exploited programmatically via the `Low Level API <LowLevelAPI.html>`_ which is based on COBRApy_.

.. _COBRApy: https://github.com/opencobra/cobrapy


For citation purposes please refer to:

.. note:: Oarga et al. **Growth Dependent Computation of Chokepoints in Metabolic Networks.** International Conference on Computational Methods in Systems Biology. Springer, Cham, 2020. https://doi.org/10.1007/978-3-030-60327-4_6 .
