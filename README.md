Empirion ontology family dedicated to empirical data variables description that supports data integration. It consists of two ontologies: empirion2 is a core ontology with key entities that provide nesessary and sufficient set of entities for variables description; empirion2_exp is its extension for the experimental data (based on the empirion ontology for experimental variables created earlier). The ontologies accompanied by a prototype for their population.

To run the example on your local machine download **empirion2_exp** folder, after this:
- In the file emp.py on the line 140 instead of C:\Users\Alena\Desktop\empirion2_exp put the path to your local copy of the main folder. 
- If you renamed the file with the ontology to be populated (empirion_pop.owl by default), change its name in the emp.py (line 141).
- Run the code.
- While the code is executed it will ask you to choose the path to the datasets for ontology population. We put some datasets and corresponding files in the sets folder, so chose it. Sometimes this window does not pop up, check the background windows, please. 
- Check the empirion_pop.owl file, it should be filled with individuals now. (The file empirion_pop_filled.owl is the example of what you should have, it contains empirion ontology filled with data from the sets forlder.)
Comments in the file emp.py are currently in Russian but feel free to ask any questions at jimijimiyo@gmail.com (Alena).

The other folders in the repository are:
- empirion1 is the first version of the ontology that was dedicated data from the behavioral experiments and prototype for its automatic population.
- ontology_versions_old with the previous ontology versions including another branch of ontology development (empirion_v4) with a direct import of reused ontologies. The file empirion.owl is always the same as the latest version of the ontology in the main branch (v 3.3 as of March 2022).
- prototype_old is a first version of the prototype based on our previous project. You can find more about it in our paper A method of semi-automated ontology population from multiple semi-structured data sources (https://doi.org/10.1177/016555152095024).

This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

The project's page and publications: https://www.researchgate.net/project/Development-of-the-knowledge-bases-from-empirical-research-datasets-ontological-approach-EMPIRION
