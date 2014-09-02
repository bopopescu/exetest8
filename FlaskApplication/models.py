import mysql.connector
import math


class Flight():
    """I am the flight class"""

    def test(self, pc,):
        cnx = mysql.connector.connect(user='sql250441', password='cA5!dR5!',
                                      host='sql2.freemysqlhosting.net',
                                      database='sql250441', buffered =True)

#         cnx = mysql.connector.connect(user='root', password='root',
#                     host='localhost',
#                               database='BRS')
        cur = cnx.cursor()

        cur.execute ('''\
        SELECT * FROM postcode WHERE postcode = (%s)''', (pc.replace(" ", ""),))
        for i in range(1):
            row1 = cur.fetchone()
            easting = row1[2]
            northing = row1[3]
            
            print  'easting is' ,easting
        
        #get the home cell and it's values
        cur.execute ('''\
        SELECT * FROM grid WHERE minNorth <= (%s) and maxNorth >= (%s) and minEast <= (%s) and maxEast >= (%s)''', (northing, northing, easting, easting ))
        for i in range(1):
            row1 = cur.fetchone()
            rowid = row1[0] - 90000
            minLat = row1[5]
            minLong = row1[6]
            maxLat = row1[7]
            maxLong = row1[8]
            value = row1[9]
            valueCol = row1[10]
            t1 = row1[11]
            t2 = row1[12]
            t3 = row1[13]
            t4 = row1[14]
            t5 = row1[15]
            t6 = row1[16]
            t7 = row1[17]
            t8 = row1[18]


        #run some logic to get the x and y
        y = int(math.ceil(rowid/300))
        x = int(rowid - ((y-1)*300))
        yOrig = int(math.ceil(rowid/300))
        xOrig = int(rowid - ((y-1)*300))

        #now get the cell id for firstRow around      
        first1 = ((y-1)*300) + x+1 #up
        first2 = ((y)*300)+ x +1 # up right
        first3 = ((y)*300)+ x #right
        first4 = ((y)*300) + (x-1) # down right
        first5 = ((y-1)*300) + (x-1) # down
        first6 = ((y-2)*300) + (x-1) # down left
        first7 = ((y-2)*300) + (x) #left
        first8 = ((y-2)*300) + (x+1) # up left
        
        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first1 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            rowid = row1[0]
            minLat1 = row1[5]
            minLong1 = row1[6]
            maxLat1 = row1[7]
            maxLong1 = row1[8]
            value1 = row1[9]
            valueCol1 = row1[10]

            
        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first2 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            minLat2 = row1[5]
            minLong2 = row1[6]
            maxLat2 = row1[7]
            maxLong2 = row1[8]
            value2 = row1[9]
            valueCol2 = row1[10]
        
        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first3 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            minLat3 = row1[5]
            minLong3 = row1[6]
            maxLat3 = row1[7]
            maxLong3 = row1[8]
            value3 = row1[9]
            valueCol3 = row1[10]
        
        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first4 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            minLat4 = row1[5]
            minLong4 = row1[6]
            maxLat4 = row1[7]
            maxLong4 = row1[8]
            value4 = row1[9]
            valueCol4 = row1[10]

        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first5 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            minLat5 = row1[5]
            minLong5 = row1[6]
            maxLat5 = row1[7]
            maxLong5 = row1[8]
            value5 = row1[9]
            valueCol5 = row1[10]

        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first6 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            minLat6 = row1[5]
            minLong6 = row1[6]
            maxLat6 = row1[7]
            maxLong6 = row1[8]
            value6 = row1[9]
            valueCol6 = row1[10]
            
        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first7 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            minLat7 = row1[5]
            minLong7 = row1[6]
            maxLat7 = row1[7]
            maxLong7 = row1[8]
            value7 = row1[9]                  
            valueCol7 = row1[10]

        cur.execute ('''\
        SELECT * FROM grid WHERE id = %s''', (first8 + 90000,))
        for i in range(1):
            row1 = cur.fetchone()
            minLat8 = row1[5]
            minLong8 = row1[6]
            maxLat8 = row1[7]
            maxLong8 = row1[8]
            value8 = row1[9]     
            valueCol8 = row1[10]
       
        result = [rowid, minLat, minLong, maxLat, maxLong, value, valueCol,
                               minLat1, minLong1, maxLat1, maxLong1, value1, valueCol1,
                               minLat2, minLong2, maxLat2, maxLong2, value2, valueCol2,
                               minLat3, minLong3, maxLat3, maxLong3, value3, valueCol3,
                               minLat4, minLong4, maxLat4, maxLong4, value4, valueCol4,
                               minLat5, minLong5, maxLat5, maxLong5, value5, valueCol5,
                               minLat6, minLong6, maxLat6, maxLong6, value6, valueCol6,
                               minLat7, minLong7, maxLat7, maxLong7, value7, valueCol7,
                               minLat8, minLong8, maxLat8, maxLong8, value8, valueCol8,
                        yOrig, xOrig, first1, t1, t2, t3, t4, t5, t6, t7,]
        
        print result[12]

        return result