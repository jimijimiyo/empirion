Empirion ontology family dedicated to empirical data variables description that supports data integration. It consists of two ontologies: empirion2 is a core ontology with key entities that provide nesessary and sufficient set of entities for variables description; empirion2_exp is its extension for the experimental data (based on the empirion ontology for experimental variables created earlier). The ontologies accompanied by a prototype for their population. The project was finished at the end of 2022 but if you have some application ides, or any comments, feel free to contact me at jimijimiyo@gmail.com (Alena).

To run the example on your local machine download **empirion2_exp** folder, after this:
- In the file emp.py on the line 140 instead of C:\Users\Alena\Desktop\empirion2_exp put the path to your local copy of the main folder. 
- If you renamed the file with the ontology to be populated (empirion_pop.owl by default), change its name in the emp.py (line 141).
- Run the code.
- While the code is executed it will ask you to choose the path to the datasets for ontology population. We put some datasets and corresponding files in the sets folder, so chose it. Sometimes this window does not pop up, check the background windows, please. 
- Check the empirion_pop.owl file, it should be filled with individuals now. (The file empirion_pop_filled.owl is the example of what you should have, it contains empirion ontology filled with data from the sets forlder.)

To run the empirion on your oen example download a folder **empirion2** and follow instructions on reuse in https://doi.org/10.13140/RG.2.2.31390.00325.

The other folders in the repository are:
- empirion1 is the first version of the ontology that was dedicated data from the behavioral experiments and prototype for its automatic population.
- ontology_versions_old with the previous ontology versions including another branch of ontology development (empirion_v4) with a direct import of reused ontologies. The file empirion.owl is always the same as the latest version of the ontology in the main branch (v 3.3 as of March 2022).
- prototype_old is a first version of the prototype based on our previous project. You can find more about it in our paper A method of semi-automated ontology population from multiple semi-structured data sources (https://doi.org/10.1177/016555152095024).

This work is licensed under the Creative Commons Attribution 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.

Main publications related to the project:
- Begler, A. (2023). An ontology of empirical research variables and a proposal for ontology development process improvement. https://doi.org/10.13140/RG.2.2.31390.00325. *A final paper with a high-level description of what's been done.*
- Begler, A., Anufriev, G., Leshcheva, I. (2022). Ontology of Experimental Variables as an Extension of Infrastructure for Behavioral Research Data FAIRification. In: Garoufallou, E., Ovalle-Perandones, MA., Vlachidis, A. (eds) Metadata and Semantic Research. MTSR 2021. Communications in Computer and Information Science, vol 1537 (pp. 268–279). Springer, Cham. https://doi.org/10.1007/978-3-030-98876-0_24. *A description of how the ontology and prototype works on a cognitive science domain.*
- Begler, A. (2019) A standard language for the description of datasets obtained in experimental studies. In Proceedings of the Posters and Demo Track of the 15th International Conference on Semantic Systems (SEMANTiCS 2019) (pp. 1–5). Retrieved from http://ceur-ws.org/Vol-2451/paper-05.pdf. *The paper from which all this started, the ontologies wasn't at use yet, but the idea is already there.*

More papers, including open versions and some texts in Russian, can be found at my ResearchGate profile: researchgate.net/profile/Alena-Begler/.
