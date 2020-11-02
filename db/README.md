### Isaiah Database

#### Database Technology: A "Tri-Lingual" Approach for Natural Language Processing

The databases used in this project are of two kinds. The first is a Relational DataBase Management System (RDBMS). For the RDBMS, I use MariaDB, an open-source relational database system. Within the MariaDB, I store many linguistic data pertaining to the Hebrew, Greek, Syriac, Aramaic, and Latin morphological tagging schemas. More importantly, this database serves as the base to create a cutting-edge method to analyse issues of translation, historical syntax, and text-critical issues, as a Hebrew text (donor language) was translated into Greek, Aramaic, Syriac, and Latin (the donor languages).

The MariaDB is generated through a python script (`create_database.py`). In this script, you will find the necessary tables for linguistic data.

The second database model is a Mongo Database (MongoDB). MongoDB contains the diplomatic transcriptions of ancient artefacts. This is a fairly straightforward database system.

The third database is currently under development. I am working to create an ancient Hebrew synset lexicon. I will explain more about this synset in the future, as it will be instrumental to perform various computational analysis of linguistic and literary analysis of ancient Hebrew, Aramaic, and Syriac texts.

The advantages to creating a "tri-lingual" database model are many. In future posts at https://jamesmtucker.com, I will elaborate in greater detail on the reasons why I designed the database as I have.

#### Database Model

#### Morphological Tagging

#### Synchronic and Diachronic Issues

#### Translation Issues: Historical Syntax and Semantic Analysis
