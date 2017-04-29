def csv_to_gj(csv, dest):
    """
    Convierte csv a GeoJson 
    :param csv: 
    :return: geoJson
    """
    file_in = open(csv)
    pref = '{  "type":"FeatureCollection",  "features": [{"type": "Feature",'
    pos = "]]}}]}"
    geo = '"geometry": { "type":"Polygon", "coordinates":  [[ '

    file_out = open(dest, "w")

    for row in file_in:
        if row[0] == "#":
            continue
        words = row.split(",")
        coor = "[" + words[1] + "," + words[0] + "],"
        geo = geo + coor

    file_out.write(pref + geo[:-1] + pos)


csv_to_gj("../data/ATMTS/2009.03.31/try2.csv", "j.json")
