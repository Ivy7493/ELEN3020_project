import unittest
import DataAPI
import sqlite3

conn = sqlite3.connect('Test.db')

#USE THIS TO ADD A USER BEFORE RUNNING TESTS - REMEMBER TO DELETE THE USER AFTER
#c = conn.cursor()
#c.execute("INSERT INTO LoginTable (username, password, accessLevel, loggedIn) VALUES (?, ?, ?, ?)",("TEST", "TEST", 2, 1))
#conn.commit()

#NOTE: NEED TO HAVE A LOGIN SET TO 1
class TestData(unittest.TestCase):

    #UNIT TEST: ADDING A FRIDGE
    def test_AddFridge(self):
        result = DataAPI.AddFridge(conn, "F29", 0, 10, 10, 100)
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteFridge(conn, "F29")
        self.assertEqual(result, "Successfully added Fridge F29")

    #UNIT TEST: ADDING A FRIDGE THAT ALREADY EXISTS
    def test_AddExistingFridge(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        result = DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result, "Successfully added Fridge F20")

    #UNIT TEST: DELETING A FRIDGE
    def test_DeleteFridge(self):
        DataAPI.AddFridge(conn, "F29", 0, 10, 10, 100)
        result = DataAPI.DeleteFridge(conn, "F29")
        print("UNIT TEST: " + str(result))
        self.assertEqual(result, "Fridge: F29 succesfully deleted!")
  
    #UNIT TEST: DELETING A FRIDGE THAT DOESN'T EXIST
    def test_DeleteNonExistentFridge(self):
        result = DataAPI.DeleteFridge(conn, "F29")
        print("UNIT TEST: " + str(result))
        self.assertEqual(result, "Fridge doesn't exist or is not empty! Cannot be deleted")

    #UNIT TEST: DELETING A FRIDGE THAT IS NOT EMPTY
    def test_DeleteNonEmptyFridge(self):
        DataAPI.AddFridge(conn, "F29", 0, 10, 10, 100)
        DataAPI.AddBox(conn, "B30", "F29", 1, 2, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B30", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.DeleteFridge(conn, "F29")
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B30")
        DataAPI.DeleteFridge(conn, "F29")
        self.assertEqual(result, "Fridge doesn't exist or is not empty! Cannot be deleted")

    #UNIT TEST: ADDING A BOX
    def test_AddSuccessfulBox(self):
        DataAPI.AddFridge(conn, "F30", 0, 10, 10, 10)
        result = DataAPI.AddBox(conn, "B30", "F30", 1, 2, 10, 10, 10)
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteBox(conn, "B30")
        DataAPI.DeleteFridge(conn, "F30")
        self.assertEqual(result,"Successfully added Box B30")  

    #UNIT TEST: ADDING A Box THAT ALREADY EXISTS
    def test_AddExistingBox(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B12", "F20", 1, 1, 1, 1, 1)
        result = DataAPI.AddBox(conn, "B12", "F20", 1, 2, 1, 1, 1)
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteBox(conn, "B12")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result, "Successfully added Box B12")

    #UNIT TEST: ADDING A BOX TO A TAKEN POSITION IN A FRIDGE 
    def test_AddBoxTakenPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B12", "F20", 1, 1, 1, 1, 1)
        result = DataAPI.AddBox(conn, "B11", "F20", 1, 1, 1, 1, 1)
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteBox(conn, "B12")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result,"Successfully added Box B11")

    #UNIT TEST: DELETING A BOX
    def test_DeleteBox(self):
        DataAPI.AddFridge(conn, "F21", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B15", "F21", 1, 2, 10, 10, 10)
        result = DataAPI.DeleteBox(conn, "B15")
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteFridge(conn, "F21")
        self.assertEqual(result,"Box: B15 succesfully deleted!")

    #UNIT TEST: MOVING A BOX
    def test_MoveBox(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 2, 10, 10, 10)
        DataAPI.AddFridge(conn, "F23", 0, 10, 10, 10)
        result = DataAPI.MoveBox(conn, "B16", "F23", 1,2)
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F23")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Box: B16 was moved to fridge: F23 (1,2)")




    #UNIT TEST: ADDING A SAMPLE
    def test_AddSampleSuccessful(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result=DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Successfully added sample S20")



    #UNIT TEST: MOVING A SAMPLE
    def test_MoveSample(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 10, 10, 10)
        DataAPI.AddBox(conn, "B17", "F22", 1, 2, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B16", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.MoveSample(conn, "S20", "B17", 1,1,1)
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteBox(conn, "B17")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Successfully moved sample: S20 into box: B17")

    #UNIT TEST: DELETING A SAMPLE
    def test_DeleteSample(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B16", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.DeleteSample(conn, "S20")
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Sample: S20 successfully deleted!")

    #UNIT TEST: ADDING A COLLECTION
    def test_AddCollection(self):
        result = DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        print("UNIT TEST: " + str(result))
        DataAPI.DeleteCollection(conn, "C10")
        self.assertEqual(result, "Successfully added Collection C10")

    #UNIT TEST: DELETING A COLLECTION
    def test_DeleteCollection(self):
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result = DataAPI.DeleteCollection(conn, "C10")
        print("UNIT TEST: " + str(result))
        self.assertEqual(result, "Collection: C10 successfully deleted!")




if __name__ == '__main__':
    unittest.main()
    conn.close()

