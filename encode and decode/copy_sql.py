from ntpath import join


tables = ["aka_name", "aka_title", "cast_info", "char_name", "comp_cast_type", "company_name", "company_type", \
    "complete_cast", "info_type", "keyword", "kind_type", "link_type", "movie_companies", "movie_info", "movie_info_idx", \
        "movie_keyword", "movie_link", "name", "person_info", "role_type", "title"]

#dict for tables
tables_dict = dict(enumerate(tables))

columns = ["aka_name.id", "aka_name.person_id", "aka_name.imdb_index", "aka_name.md5sum", "aka_name.name", "aka_name.name_pcode_cf", "aka_name.name_pcode_nf", \
    "aka_name.surname_pcode", "aka_title.id", "aka_title.movie_id", "aka_title.episode_nr", "aka_title.episode_of_id", "aka_title.imdb_index", "aka_title.kind_id", "aka_title.md5sum",\
    "aka_title.note", "aka_title.phonetic_code", "aka_title.production_year", "aka_title.season_nr", "aka_title.title", "cast_info.id", "cast_info.movie_id", "cast_info.person_id", "cast_info.person_role_id", "cast_info.role_id", \
    "cast_info.note", "cast_info.nr_order", "char_name.id", "char_name.imdb_id", "char_name.imdb_index", "char_name.md5sum", "char_name.name", "char_name.name_pcode_nf", "char_name.surname_pcode", \
    "comp_cast_type.id", "comp_cast_type.kind", "company_name.id", "company_name.country_code", "company_name.imdb_id", "company_name.md5sum", "company_name.name", "company_name.name_pcode_nf", "company_name.name_pcode_sf", \
    "company_type.id", "company_type.kind", "complete_cast.id", "complete_cast.subject_id", "complete_cast.status_id", "complete_cast.movie_id", "info_type.id", "info_type.info", "keyword.id", "keyword.keyword", "keyword.phonetic_code", "kind_type.id", "kind_type.kind", \
    "link_type.id", "link_type.link", "movie_companies.id", "movie_companies.company_id", "movie_companies.movie_id", "movie_companies.company_type_id", "movie_info.id", "movie_info.movie_id", "movie_info.info_type_id", "movie_info.info", "movie_info.note", \
    "movie_info_idx.id", "movie_info_idx.movie_id", "movie_info_idx.info_type_id", "movie_info_idx.info", "movie_info_idx.note", "movie_keyword.id", "movie_keyword.movie_id", "movie_keyword.keyword_id", "movie_link.id", "movie_link.movie_id", "movie_link.linked_movie_id", \
    "movie_link.link_type_id", "name.id", "name.gender", "name.imdb_id", "name.imdb_index", "name.md5sum", "name.name", "name.name_pcode_cf", "name.name_pcode_nf", "name.surname_pcode", "person_info.id", "person_info.info_type_id", "person_info.person_id", "person_info.info", "person_info.note", \
    "role_type.id", "role_type.role", "title.id", "title.kind_id", "title.episode_nr", "title.episode_of_id", "title.imdb_index", "title.kind_id", "title.md5sum", "title.phonetic_code", "title.production_year", "title.season_nr", "title.series_years"]

#dict for columns
columns_dict = dict(enumerate(columns))








#TESTEN
test = []
seq = "101010"
for x in seq:
    test.append(int(x))
first = test[:3]
second = test[3:5]
third = test[5:6]
print(first)
print(second)
print(third)