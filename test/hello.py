import pypyodbc as pyodbc
cnxn = pyodbc.connect('DRIVER={PostgreSQL Unicode};Server=127.0.0.1;Port=5432;Database=imdbload;UID=postgres;password=bachelor;String Types=Unicode')
cursor = cnxn.cursor()
#cursor.execute("SELECT MIN(link_type.link) AS link_type, MIN(t1.title) AS first_movie, MIN(t2.title) AS second_movie \
#    INTO TEMP TABLE test \
#        FROM keyword, link_type, movie_keyword, movie_link, title AS t1, title AS t2 \
#             WHERE keyword.keyword='character-name-in-title' \
#                 AND movie_keyword.keyword_id=keyword.id \
#                     AND t1.id=movie_keyword.movie_id \
#                         AND movie_link.movie_id=t1.id \
#                             AND movie_link.linked_movie_id=t2.id \
#                                 AND link_type.id=movie_link.link_type_id \
#                                     AND movie_keyword.movie_id=t1.id")
l = "SELECT MIN(cn.name) AS movie_company, MIN(mi_idx.info) AS rating, MIN(t.title) AS mainstream_movie INTO TEMP TABLE test FROM company_name AS cn, company_type AS ct, info_type AS it1, info_type AS it2, movie_companies AS mc, movie_info AS mi, movie_info_idx AS mi_idx,title AS t WHERE cn.country_code = '[us]' AND ct.kind = 'production companies' AND it1.info = 'genres' AND it2.info = 'rating' AND mi.info IN ('Drama','Horror','Western','Family') AND mi_idx.info > '7.0' AND t.production_year BETWEEN 2000 AND 2010 AND t.id = mi.movie_id AND t.id = mi_idx.movie_id AND mi.info_type_id = it1.id AND mi_idx.info_type_id = it2.id AND t.id = mc.movie_id AND ct.id = mc.company_type_id AND cn.id = mc.company_id AND mc.movie_id = mi.movie_id AND mc.movie_id = mi_idx.movie_id AND mi.movie_id = mi_idx.movie_id;"
cursor.execute(l)
cursor.execute('SELECT * FROM test')
for i in cursor:
    print(i)
