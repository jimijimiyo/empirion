Empirion ontology for the description of data from the behavioral experiments and prototype for its automatic population.

To run it on your local machine download **main** folder, after this:
- In the file emp.py on the line 138 instead of C:\Users\Alena\Downloads put the path to your local copy of the main folder. 
- If you renamed the file with the ontology to be populated (empirion_pop.owl by default), change its name in the emp.py (line 139).
- Run the code.
- While the code is executed it will ask you to choose the path to the datasets for ontology population. We put some datasets and corresponding files in the sets folder, so chose it. Sometimes this window does not pop up, check the background windows, please. 
- Check the empirion_pop.owl file, it should be filled with individuals now.
Comments in the file emp.py are currently in Russian but we will add english comments soon! For now feel free to ask any questions at jimijimiyo@gmail.com (Alena).

The other folders in the repository are:
- ontology_versions with the previous ontology versions including another branch of ontology development (empirion_v4) with a direct import of reused ontologies. The file empirion.owl is always the same as the latest version of the ontology in the main branch (v 3.3 as of March 2022).
- prototype_old is a first version of the prototype based on our previous project. You can find more about it in our paper A method of semi-automated ontology population from multiple semi-structured data sources (https://doi.org/10.1177/0165551520950243).

The project's page and publications: https://www.researchgate.net/project/Development-of-the-knowledge-bases-from-empirical-research-datasets-ontological-approach-EMPIRION
