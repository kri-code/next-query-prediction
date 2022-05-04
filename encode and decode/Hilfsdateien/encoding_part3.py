#Anfrage 1a
["company_type.kind =", "info_type.info =", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "movie_companies.note OR"]
#Anfrage 1b 
["company_type.kind =", "info_type.info =", "movie_companies.note NOT LIKE", "title.production_year BETWEEN"]
#Anfrage 1c
["company_type.kind =", "info_type.info =", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "title.production_year >"]
#Anfrage 1d
["company_type.kind =", "info_type.info =", "movie_companies.note NOT LIKE", "title.production_year >"]
#Anfrage 2a
["company_name.country_code =", "keyword.keyword ="]
#Anfrage 2b
["company_name.country_code =", "keyword.keyword ="]
#Anfrage 2c
["company_name.country_code =", "keyword.keyword ="]
#Anfrage 2d
["company_name.country_code =", "keyword.keyword ="]
#Anfrage 3a
["keyword.keyword LIKE", "movie_info.info IN", "title.production_year >"]
#Anfrage 3b
["keyword.keyword LIKE", "movie_info.info IN", "title.production_year >"]
#Anfrage 3c
["keyword.keyword LIKE", "movie_info.info IN", "title.production_year >"]
#Anfrage 4a
["info_type.info =", "keyword.keyword LIKE", "movie_info_idx.info >", "title.production_year >"]
#Anfrage 4b
["info_type.info =", "keyword.keyword LIKE", "movie_info_idx.info >", "title.production_year >"]
#Anfrage 4c
["info_type.info =", "keyword.keyword LIKE", "movie_info_idx.info >", "title.production_year >"]
#Anfrage 5a
["company_type.kind =", "movie_companies.note LIKE", "movie_info.info IN", "title.production_year >"]
#Anfrage 5b
["company_type.kind =", "movie_companies.note LIKE", "movie_info.info IN", "title.production_year >"]
#Anfrage 5c
["company_type.kind =", "movie_companies.note LIKE", "movie_companies.note NOT LIKE", "movie_info.info IN", "title.production_year >"]
#Anfrage 6a
["keyword.keyword =", "name.name LIKE", "title.production_year >"]
#Anfrage 6b
["keyword.keyword IN", "name.name LIKE", "title.production_year >"]
#Anfrage 6c
["keyword.keyword =", "name.name LIKE", "title.production_year >"]
#Anfrage 6d
["keyword.keyword IN", "name.name LIKE", "title.production_year >"]
#Anfrage 6e
["keyword.keyword =", "name.name LIKE", "title.production_year >"]
#Anfrage 6f
["keyword.keyword IN", "title.production_year >"]
#Anfrage 7a
["aka_name.name LIKE", "info_type.info =", "link_type.link =", "name.name_pcode_cf BETWEEN", "name.gender =", "name.gender OR", "name.name LIKE", "name.name OR", "person_info.note =", "title.production_year BETWEEN"]
#Anfrage 7b
["aka_name.name LIKE", "info_type.info =", "link_type.link =", "name.name_pcode_cf LIKE", "name.gender =", "person_info.note =", "title.production_year BETWEEN"]
#Anfrage 7c
["aka_name.name =", "aka_name.name LIKE", "aka_name.name OR", "info_type.info =", "link_type.link IN", "name.name_pcode_cf BETWEEN", "name.gender =", "name.gender OR", "name.name LIKE", "name.name OR", "person_info.note =", "title.production_year BETWEEN"]
#Anfrage 8a
["cast_info.note =", "company_name.country_code =", "movie_companies.note LIKE", "movie_companies.note NOT LIKE", "name.name LIKE", "name.name NOT LIKE", "role_type.role ="]
#Anfrage 8b
["cast_info.note =", "company_name.country_code =", "movie_companies.note LIKE", "movie_companies.note NOT LIKE", "movie_companies.note OR", "name.name LIKE", "name.name NOT LIKE", "role_type.role =", "title.production_year BETWEEN", "title.title LIKE", "title.title OR"]
#Anfrage 8c
["company_name.country_code =", "role_type.role ="]
#Anfrage 8d
["company_name.country_code =", "role_type.role ="]
#Anfrage 9a
["cast_info.note IN", "company_name.country_code =", "movie_companies.note =", "movie_companies.note LIKE", "movie_companies.note OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.production_year BETWEEN"]
#Anfrage 9b
["cast_info.note =", "company_name.country_code =", "movie_companies.note LIKE", "movie_companies.note OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.production_year BETWEEN"]
#Anfrage 9c
["cast_info.note IN", "company_name.country_code =", "name.gender =", "name.name LIKE", "role_type.role ="]
#Anfrage 9d
["cast_info.note IN", "company_name.country_code =", "name.gender =", "role_type.role ="]
#Anfrage 10a
["cast_info.note LIKE", "company_name.country_code =", "role_type.role =", "title.production_year >"]
#Anfrage 10b
["cast_info.note LIKE", "company_name.country_code =", "role_type.role =", "title.production_year >"]
#Anfrage 10c
["cast_info.note LIKE", "company_name.country_code =", "title.production_year >"]
#Anfrage 11a
["company_name.country_code !=", "company_name.name LIKE", "company_name.name OR", "company_type.kind =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "title.production_year BETWEEN"]
#Anfrage 11b
["company_name.country_code !=", "company_name.name LIKE", "company_name.name OR", "company_type.kind =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "title.production_year =", "title.title LIKE"]
#Anfrage 11c
["company_name.country_code !=", "company_name.name LIKE", "company_name.name OR", "company_type.kind =", "company_type.kind !=", "keyword.keyword IN", "movie_companies.note =", "title.production_year >"]
#Anfrage 11d
["company_name.country_code !=", "company_type.kind =", "company_type.kind !=", "keyword.keyword IN", "movie_companies.note =", "title.production_year >"]
#Anfrage 12a
["company_name.country_code =", "company_type.kind =", "info_type.info =", "it2.info =", "movie_info.info IN", "movie_info_idx.info >", "title.production_year BETWEEN"]
#Anfrage 12b
["company_name.country_code =", "company_type.kind =", "company_type.kind OR", "info_type.info =", "it2.info =", "title.production_year >", "title.title LIKE", "title.title OR"]
#Anfrage 12c
["company_name.country_code =", "company_type.kind =", "info_type.info =", "it2.info =", "movie_info.info IN", "movie_info_idx.info >", "title.production_year BETWEEN"]
#Anfrage 13a
["company_name.country_code =", "company_type.kind =", "info_type.info =", "it2.info =", "kind_type.kind ="]
#Anfrage 13b
["company_name.country_code =", "company_type.kind =", "info_type.info =", "it2.info =", "kind_type.kind =", "title.title !=", "title.title LIKE", "title.title OR"]
#Anfrage 13c
["company_name.country_code =", "company_type.kind =", "info_type.info =", "it2.info =", "kind_type.kind =", "title.title !=", "title.title LIKE", "title.title OR"]
#Anfrage 13d
["company_name.country_code =", "company_type.kind =", "info_type.info =", "it2.info =", "kind_type.kind ="]
#Anfrage 14a
["info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.kind =", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 14b
["info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.kind =", "movie_info.info IN", "movie_info_idx.info >", "title.production_year >", "title.title LIKE", "title.title OR"]
#Anfrage 14c
["info_type.info =", "it2.info =", "keyword.keyword =", "keyword.keyword IN", "kind_type.kind IN", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 15a
["company_name.country_code =", "info_type.info =", "movie_companies.note LIKE", "movie_info.info LIKE", "movie_info.note LIKE", "title.production_year >"]
#Anfrage 15b
["company_name.country_code =", "company_name.name =", "info_type.info =", "movie_companies.note LIKE", "movie_info.info LIKE", "movie_info.note LIKE", "title.production_year BETWEEN"]
#Anfrage 15c
["company_name.country_code =", "info_type.info =", "movie_info.info =", "movie_info.note LIKE", "movie_info.info LIKE", "movie_info.info OR", "title.production_year >"]
#Anfrage 15d
["company_name.country_code =", "info_type.info =", "movie_info.note LIKE", "title.production_year >"]
#Anfrage 16a
["company_name.country_code =", "keyword.keyword =", "title.episode_nr >=", "title.episode_nr <"]
#Anfrage 16b
["company_name.country_code =", "keyword.keyword ="]
#Anfrage 16c
["company_name.country_code =", "keyword.keyword =", "title.episode_nr <"]
#Anfrage 16d
["company_name.country_code =", "keyword.keyword =", "title.episode_nr >=", "title.episode_nr <"]
#Anfrage 17a
["company_name.country_code =", "keyword.keyword =", "name.name LIKE"]
#Anfrage 17b
["keyword.keyword =", "name.name LIKE"]
#Anfrage 17c
["keyword.keyword =", "name.name LIKE"]
#Anfrage 17d
["keyword.keyword =", "name.name LIKE"]
#Anfrage 17e
["company_name.country_code =", "keyword.keyword ="]
#Anfrage 17f
["keyword.keyword =", "name.name LIKE"]
#Anfrage 18a
["cast_info.note IN", "info_type.info =", "it2.info =", "name.gender =", "name.name LIKE"]
#Anfrage 18b
["cast_info.note IN", "info_type.info =", "it2.info =", "movie_info.info IN", "movie_info.note IS NULL", "movie_info_idx.info >", "name.gender =", "title.production_year BETWEEN"]
#Anfrage 18c
["cast_info.note IN", "info_type.info =", "it2.info =", "movie_info.info IN", "name.gender ="]
#Anfrage 19a
["cast_info.note IN", "company_name.country_code =", "info_type.info =", "movie_companies.note =", "movie_companies.note LIKE", "movie_companies.note OR", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.production_year BETWEEN"]
#Anfrage 19b
["cast_info.note =", "company_name.country_code =", "info_type.info =", "movie_companies.note LIKE", "movie_companies.note OR", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.production_year BETWEEN", "title.title LIKE"]
#Anfrage 19c
["cast_info.note IN", "company_name.country_code =", "info_type.info =", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.production_year >"]
#Anfrage 19d
["cast_info.note IN", "company_name.country_code =", "info_type.info =", "name.gender =", "role_type.role =", "title.production_year >"]
#Anfrage 20a
["comp_cast_type.kind =", "cct2.kind LIKE", "char_name.name NOT LIKE", "char_name.name LIKE", "char_name.name OR", "keyword.keyword IN", "kind_type.type =", "title.production_year >"]
#Anfrage 20b
["comp_cast_type.kind =", "cct2.kind LIKE", "char_name.name NOT LIKE", "char_name.name LIKE", "char_name.name OR", "keyword.keyword IN", "kind_type.type =", "name.name LIKE", "title.production_year >"]
#Anfrage 20c
["comp_cast_type.kind =", "cct2.kind LIKE", "char_name.name =", "char_name.name LIKE", "char_name.name OR", "keyword.keyword IN", "kind_type.type =", "title.production_year >"]
#Anfrage 21a
["company_name.country_code !=", "company_name.name LIKE", "company_name.name OR", "company_type =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "movie_info.info IN", "title.production_year BETWEEN"]
#Anfrage 21b
["company_name.country_code !=", "company_name.name LIKE", "company_name.name OR", "company_type =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "movie_info.info IN", "title.production_year BETWEEN"]
#Anfrage 21c
["company_name.country_code !=", "company_name.name LIKE", "company_name.name OR", "company_type =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "movie_info.info IN", "title.production_year BETWEEN"]
#Anfrage 22a
["company_name.country_code !=", "info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.type IN", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 22b
["company_name.country_code !=", "info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.type IN", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 22c
["company_name.country_code !=", "info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.type IN", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 22d
["company_name.country_code !=", "info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.type IN", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 23a
["comp_cast_type.kind =", "company_name.country_code =", "info_type.info =", "kind_type.type IN", "movie_info.note LIKE", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "title.production_year >"]
#Anfrage 23b
["comp_cast_type.kind =", "company_name.country_code =", "info_type.info =", "keyword.keyword IN", "kind_type.type IN", "movie_info.note LIKE", "movie_info.info LIKE", "title.production_year >"]
#Anfrage 23c
["comp_cast_type.kind =", "company_name.country_code =", "info_type.info =", "kind_type.type IN", "movie_info.note LIKE", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "title.production_year >"]
#Anfrage 24a
["cast_info.note IN", "company_name.country_code =", "info_type.info =", "keyword.keyword IN", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.production_year >"]
#Anfrage 24b
["cast_info.note IN", "company_name.country_code =", "company_name.name =", "info_type.info =", "keyword.keyword IN", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.production_year >", "title.title LIKE"]
#Anfrage 25a
["cast_info.note IN", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info =", "name.gender ="]
#Anfrage 25b
["cast_info.note IN", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info =", "name.gender =", "title.production_year >", "title.title LIKE"]
#Anfrage 25c
["cast_info.note IN", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info IN", "name.gender ="]
#Anfrage 26a
["comp_cast_type.kind =", "cct2.kind LIKE", "char_name.name =", "char_name.name LIKE", "char_name.name OR", "it2.info =", "keyword.keyword IN", "kind_type.type =", "movie_info_idx.info >", "title.production_year >"]
#Anfrage 26b
["comp_cast_type.kind =", "cct2.kind LIKE", "char_name.name =", "char_name.name LIKE", "char_name.name OR", "it2.info =", "keyword.keyword IN", "kind_type.type =", "movie_info_idx.info >", "title.production_year >"]
#Anfrage 26c
["comp_cast_type.kind =", "cct2.kind LIKE", "char_name.name =", "char_name.name LIKE", "char_name.name OR", "it2.info =", "keyword.keyword IN", "kind_type.type =", "title.production_year >"]
#Anfrage 27a
["comp_cast_type.kind IN", "cct2.kind =", "company_name.country_code !=", "char_name.name LIKE", "char_name.name OR", "company_type.kind =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "movie_info.info IN", "title.production_year BETWEEN"]
#Anfrage 27b
["comp_cast_type.kind IN", "cct2.kind =", "company_name.country_code !=", "char_name.name LIKE", "char_name.name OR", "company_type.kind =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "movie_info.info IN", "title.production_year ="]
#Anfrage 27c
["comp_cast_type.kind =", "cct2.kind LIKE", "company_name.country_code !=", "char_name.name LIKE", "char_name.name OR", "company_type.kind =", "keyword.keyword =", "link_type.link LIKE", "movie_companies.note IS NULL", "movie_info.info IN", "title.production_year BETWEEN"]
#Anfrage 28a
["comp_cast_type.kind =", "cct2.kind !=", "company_name.country_code !=", "info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.type IN", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 28b
["comp_cast_type.kind =", "cct2.kind !=", "company_name.country_code !=", "info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.type IN", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "movie_info.info IN", "movie_info_idx.info >", "title.production_year >"]
#Anfrage 28c
["comp_cast_type.kind =", "cct2.kind =", "company_name.country_code !=", "info_type.info =", "it2.info =", "keyword.keyword IN", "kind_type.type IN", "movie_companies.note NOT LIKE", "movie_companies.note LIKE", "movie_info.info IN", "movie_info_idx.info <", "title.production_year >"]
#Anfrage 29a
["comp_cast_type.kind =", "cct2.kind =", "char_name.name =", "cast_info.note IN", "company_name.country_code =", "info_type.info =", "it2.info =", "keyword.keyword =", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.title =", "title.production_year BETWEEN"]
#Anfrage 29b
["comp_cast_type.kind =", "cct2.kind =", "char_name.name =", "cast_info.note IN", "company_name.country_code =", "info_type.info =", "it2.info =", "keyword.keyword =", "movie_info.info LIKE", "name.gender =", "name.name LIKE", "role_type.role =", "title.title =", "title.production_year BETWEEN"]
#Anfrage 29c
["comp_cast_type.kind =", "cct2.kind =", "cast_info.note IN", "company_name.country_code =", "info_type.info =", "it2.info =", "keyword.keyword =", "movie_info.info =", "movie_info.info LIKE", "movie_info.info OR", "name.gender =", "name.name LIKE", "role_type.role =", "title.title =", "title.production_year BETWEEN"]
#Anfrage 30a
["comp_cast_type.kind IN", "cct2.kind =", "cast_info.note IN", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info IN", "name.gender =", "title.production_year >"]
#Anfrage 30b
["comp_cast_type.kind IN", "cct2.kind =", "cast_info.note IN", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info IN", "name.gender =", "title.production_year >", "title.title LIKE", "title.title OR"]
#Anfrage 30c
["comp_cast_type.kind =", "cct2.kind =", "cast_info.note IN", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info IN", "name.gender ="]
#Anfrage 31a
["cast_info.note IN", "company_name.name LIKE", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info IN", "name.gender ="]
#Anfrage 31b
["cast_info.note IN", "company_name.name LIKE", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_companies.note LIKE", "movie_info.info IN", "name.gender =", "title.production_year >", "title.title LIKE", "title.title OR"]
#Anfrage 31c
["cast_info.note IN", "company_name.name LIKE", "info_type.info =", "it2.info =", "keyword.keyword IN", "movie_info.info IN"]
#Anfrage 32a
["keyword.keyword ="]
#Anfrage 32b
["keyword.keyword ="]
#Anfrage 33a
["company_name.country_code =", "info_type.info =", "it2.info =", "kind_type.type IN", "kt2.type IN", "link_type.link IN", "mi_idx2.info <", "t2.production_year BETWEEN"]
#Anfrage 33b
["company_name.country_code =", "info_type.info =", "it2.info =", "kind_type.type IN", "kt2.type IN", "link_type.link LIKE", "mi_idx2.info <", "t2.production_year ="]
#Anfrage 33c
["company_name.country_code !=", "info_type.info =", "it2.info =", "kind_type.type IN", "kt2.type IN", "link_type.link IN", "mi_idx2.info <", "t2.production_year BETWEEN"]