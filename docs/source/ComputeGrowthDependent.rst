
Compute growth dependent chokepoints
====================================

findCPcli allows, from a model in SBML format, to calculate how refining the model with different values of the fraction of the optimum with FVA affects the number of chokepoints
(i.e. `Growth Dependent Chokepoints <https://doi.org/10.1007/978-3-030-60327-4_6>`_).
, reversible and non reversible reactions and dead reactions (i.e. reactions with upper and lower bound equal to 0).
The tool produces a spreadsheet file showing how the size of these set varies.

::

    $ findCPcli -i model.xml -cp generate_output.xls 


Pipeline pseudocode
********************

The pipeline pseudocode of this operation is included below:

::

    model = read_model()
    initial_reversible_reactions     = all reactions with upper flux bound > 0 and lower flux bound < 0
    initial_dead_reactions           = all reactions with both upper and lower flux bound equal to 0
    initial_non_reversible_reactions = model.reactions - reversible_reactions - dead_reactions
    initial_chokepoint_reactions     = find_chokepoints(model)
    
    for fraction in [0,0 ... 1,0]
        model = read_model()
        model = update_flux_bounds_with_fva(model, fraction)
        reversible_reactions[fraction]     = all reactions with upper flux bound > 0 and lower flux bound < 0
        dead_reactions[fraction]           = all reactions with both upper and lower flux bound equal to 0
        non_reversible_reactions[fraction] = model.reactions - reversible_reactions - dead_reactions
        chokepoint_reactions[fraction]     = find_chokepoints(model)
