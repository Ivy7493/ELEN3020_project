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

    #UNIT TEST 1: ADDING A FRIDGE
    def test_AddFridge(self):
        result = DataAPI.AddFridge(conn, "F29", 0, 10, 10, 100)
        print("UNIT TEST 1: " + str(result))
        DataAPI.DeleteFridge(conn, "F29")
        self.assertEqual(result, "Successfully added Fridge F29")

    #UNIT TEST 2: ADDING A FRIDGE THAT ALREADY EXISTS
    def test_AddExistingFridge(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        result = DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        print("UNIT TEST 2: " + str(result))
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result, "Successfully added Fridge F20")

    #UNIT TEST 3: DELETING A FRIDGE
    def test_DeleteFridge(self):
        DataAPI.AddFridge(conn, "F29", 0, 10, 10, 100)
        result = DataAPI.DeleteFridge(conn, "F29")
        print("UNIT TEST 3: " + str(result))
        self.assertEqual(result, "Fridge F29 successfully deleted")
  
    #UNIT TEST 4: DELETING A FRIDGE THAT DOESN'T EXIST
    def test_DeleteNonExistentFridge(self):
        result = DataAPI.DeleteFridge(conn, "F29")
        print("UNIT TEST 4: " + str(result))
        self.assertEqual(result, "Fridge does not exist or is not empty - cannot be deleted")

    #UNIT TEST 5: DELETING A FRIDGE THAT IS NOT EMPTY
    def test_DeleteNonEmptyFridge(self):
        DataAPI.AddFridge(conn, "F29", 0, 10, 10, 100)
        DataAPI.AddBox(conn, "B30", "F29", 1, 2, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B30", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.DeleteFridge(conn, "F29")
        print("UNIT TEST 5: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B30")
        DataAPI.DeleteFridge(conn, "F29")
        self.assertEqual(result, "Fridge does not exist or is not empty - cannot be deleted")

    #UNIT TEST 6: ADDING A BOX
    def test_AddSuccessfulBox(self):
        DataAPI.AddFridge(conn, "F30", 0, 10, 10, 10)
        result = DataAPI.AddBox(conn, "B30", "F30", 1, 2, 10, 10, 10)
        print("UNIT TEST 6: " + str(result))
        DataAPI.DeleteBox(conn, "B30")
        DataAPI.DeleteFridge(conn, "F30")
        self.assertEqual(result,"Successfully added Box B30")  

    #UNIT TEST 7: ADDING A Box THAT ALREADY EXISTS
    def test_AddExistingBox(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B12", "F20", 1, 1, 1, 1, 1)
        result = DataAPI.AddBox(conn, "B12", "F20", 1, 2, 1, 1, 1)
        print("UNIT TEST 7: " + str(result))
        DataAPI.DeleteBox(conn, "B12")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result, "Successfully added Box B12")

    #UNIT TEST 8: ADDING A BOX TO A TAKEN POSITION IN A FRIDGE 
    def test_AddBoxTakenPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B12", "F20", 1, 1, 1, 1, 1)
        result = DataAPI.AddBox(conn, "B11", "F20", 1, 1, 1, 1, 1)
        print("UNIT TEST 8: " + str(result))
        DataAPI.DeleteBox(conn, "B12")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result,"Successfully added Box B11")

    #UNIT TEST 9: DELETING A BOX
    def test_DeleteBox(self):
        DataAPI.AddFridge(conn, "F21", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B15", "F21", 1, 2, 10, 10, 10)
        result = DataAPI.DeleteBox(conn, "B15")
        print("UNIT TEST 9: " + str(result))
        DataAPI.DeleteFridge(conn, "F21")
        self.assertEqual(result,"Box B15 successfully deleted")

    #UNIT TEST 10: DELETING A BOX THAT DOESN'T EXIST
    def test_DeleteNonExistentBox(self):
        result = DataAPI.DeleteBox(conn, "F29")
        print("UNIT TEST 10: " + str(result))
        self.assertEqual(result, "Box does not exist or is not empty - cannot be deleted")

    #UNIT TEST 11: DELETING A BOX THAT IS NOT EMPTY
    def test_DeleteNonEmptyBox(self):
        DataAPI.AddFridge(conn, "F29", 0, 10, 10, 100)
        DataAPI.AddBox(conn, "B30", "F29", 1, 2, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B30", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.DeleteBox(conn, "B30")
        print("UNIT TEST 11: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B30")
        DataAPI.DeleteFridge(conn, "F29")
        self.assertEqual(result, "Box does not exist or is not empty - cannot be deleted")

    #UNIT TEST 12: MOVING A BOX
    def test_MoveBox(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 2, 10, 10, 10)
        DataAPI.AddFridge(conn, "F23", 0, 10, 10, 10)
        result = DataAPI.MoveBox(conn, "B16", "F23", 1,2)
        print("UNIT TEST 12: " + str(result))
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F23")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Box B16 was moved to Fridge F23 (1,2)")

    #UNIT TEST 13: MOVING A BOX TO NON EXISTENT FRIDGE
    def test_MoveBoxNonExistingFridge(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 2, 10, 10, 10)
        result = DataAPI.MoveBox(conn, "B16", "F23", 1, 2)
        print("UNIT TEST 13: " + str(result))
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Fridge ID F23 does not exist")

    #UNIT TEST 14: MOVING A NON EXISTENT BOX
    def test_MoveNonExistingBox(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        result = DataAPI.MoveBox(conn, "B16", "F22", 1, 1)
        print("UNIT TEST 14: " + str(result))
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Box ID B16 does not exist")

    #UNIT TEST 15: MOVING A BOX TO A TAKEN POSITION IN A FRIDGE 
    def test_MoveBoxTakenPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B13", "F20", 1, 1, 1, 1, 1)
        DataAPI.AddBox(conn, "B12", "F20", 1, 2, 1, 1, 1)
        result = DataAPI.MoveBox(conn, "B12", "F20", 1, 1)
        print("UNIT TEST 15: " + str(result))
        DataAPI.DeleteBox(conn, "B12")
        DataAPI.DeleteBox(conn, "B13")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Position already taken")

    #UNIT TEST 16: MOVING A BOX TO AN INVALID X POSITION IN A FRIDGE 
    def test_MoveBoxInvalidXPos(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 100)
        DataAPI.AddBox(conn, "B13", "F20", 1, 1, 1, 1, 1)
        result = DataAPI.MoveBox(conn, "B13", "F20", 100, 1)
        print("UNIT TEST 16: " + str(result))
        DataAPI.DeleteBox(conn, "B13")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid X location")

    #UNIT TEST 17: MOVING A BOX TO AN INVALID Y POSITION IN A FRIDGE 
    def test_MoveBoxInvalidYPos(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 100)
        DataAPI.AddBox(conn, "B13", "F20", 1, 1, 1, 1, 1)
        result = DataAPI.MoveBox(conn, "B13", "F20", 1, 100)
        print("UNIT TEST 17: " + str(result))
        DataAPI.DeleteBox(conn, "B13")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid Y location")

    #UNIT TEST 18: ADDING A SAMPLE
    def test_AddSampleSuccessful(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result=DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 18: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Successfully added sample S20")

    #UNIT TEST 19: ADDING A SAMPLE THAT ALREADY EXISTS
    def test_AddSampleAlreadyExist(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result=DataAPI.AddSample(conn, "S20", "B10", 1, 1, 2, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 19: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result,"Successfully added sample S20")

    #UNIT TEST 20: ADDING A SAMPLE TO TAKEN POSITION
    def test_AddSampleTakenPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result=DataAPI.AddSample(conn, "S21", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 20: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result,"Successfully added sample S20")

    #UNIT TEST 21: ADDING A SAMPLE TO NON EXISTENT COLLECTION
    def test_AddSampleNonExistingCollection(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        result=DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 21: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Collection C10 does not exist")

    #UNIT TEST 22: ADDING A SAMPLE TO NON EXISTENT BOX
    def test_AddSampleNonExistingBox(self):
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result=DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 22: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")
        self.assertEqual(result,"Box B10 does not exist")

    #UNIT TEST 23: ADDING A SAMPLE TO INVALID X BOX POSITION
    def test_AddSampleInvalidXPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result=DataAPI.AddSample(conn, "S20", "B10", 100,1,1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 23: " + str(result))
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid X location in box B10")

    #UNIT TEST 24: ADDING A SAMPLE TO INVALID Y BOX POSITION
    def test_AddSampleInvalidYPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result=DataAPI.AddSample(conn, "S20", "B10", 1,100,1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 24: " + str(result))
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid Y location in box B10")

    #UNIT TEST 25: ADDING A SAMPLE TO INVALID Z BOX POSITION
    def test_AddSampleInvalidZPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result=DataAPI.AddSample(conn, "S20", "B10", 1,1,100, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        print("UNIT TEST 25: " + str(result))
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid Z location in box B10")

    #UNIT TEST 26: MOVING A SAMPLE
    def test_MoveSample(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 10, 10, 10)
        DataAPI.AddBox(conn, "B17", "F22", 1, 2, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B16", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.MoveSample(conn, "S20", "B17", 1,1,1)
        print("UNIT TEST 26: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteBox(conn, "B17")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Successfully moved Sample ID S20 into Box B17")

    #UNIT TEST 27: MOVING A SAMPLE TO NON EXISTENT BOX
    def test_MoveSampleNonExistingBox(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B16", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.MoveSample(conn, "S20", "B17", 1,1,1)
        print("UNIT TEST 27: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Box ID B17 does not exist")

    #UNIT TEST 28: MOVING A NON EXISTENT SAMPLE
    def test_MoveNonExistingSample(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 10, 10, 10)
        result = DataAPI.MoveSample(conn, "S20", "B16", 1,1,1)
        print("UNIT TEST 28: " + str(result))
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Sample ID S20 does not exist")

    #UNIT TEST 29: MOVING A SAMPLE TO A FULL BOX
    def test_MoveSampleToFullBox(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 1, 1, 1)
        DataAPI.AddBox(conn, "B17", "F22", 1, 2, 1, 1, 1)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B16", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        DataAPI.AddSample(conn, "S21", "B17", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.MoveSample(conn, "S21", "B16", 1,1,1)
        print("UNIT TEST 29: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteSample(conn, "S21")
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteBox(conn, "B17")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Box B16 is full - please select another box")

    #UNIT TEST 30: MOVING A SAMPLE TO INVALID X BOX POSITION
    def test_MoveSampleInvalidXPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.MoveSample(conn, "S20", "B10", 100, 1, 1)        
        print("UNIT TEST 30: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid X location in box B10")

    #UNIT TEST 31: MOVING A SAMPLE TO INVALID Y BOX POSITION
    def test_MoveSampleInvalidYPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.MoveSample(conn, "S20", "B10", 1, 100, 1)        
        print("UNIT TEST 31: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid Y location in box B10")

    #UNIT TEST 32: MOVING A SAMPLE TO INVALID Z BOX POSITION
    def test_MoveSampleInvalidZPosition(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.MoveSample(conn, "S20", "B10", 1, 1, 100)        
        print("UNIT TEST 32: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Invalid Z location in box B10")

    #UNIT TEST 33: DELETING A SAMPLE
    def test_DeleteSample(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B16", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.DeleteSample(conn, "S20")
        print("UNIT TEST 33: " + str(result))
        DataAPI.DeleteCollection(conn, "C10")
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Sample S20 successfully deleted")

    #UNIT TEST 34: DELETING A NON EXISTENT SAMPLE
    def test_DeleteSampleNonExisting(self):
        result = DataAPI.DeleteSample(conn, "S20")
        print("UNIT TEST 34: " + str(result))
        self.assertEqual(result,"Sample ID S20 does not exist")

    #UNIT TEST 35: ADDING A COLLECTION
    def test_AddCollection(self):
        result = DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        print("UNIT TEST 35: " + str(result))
        DataAPI.DeleteCollection(conn, "C10")
        self.assertEqual(result, "Successfully added Collection C10")

    #UNIT TEST 36: DELETING A COLLECTION
    def test_DeleteCollection(self):
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        result = DataAPI.DeleteCollection(conn, "C10")
        print("UNIT TEST 36: " + str(result))
        self.assertEqual(result, "Collection C10 successfully deleted")

    #UNIT TEST 37: DELETING A NON EXISTENT COLLECTION
    def test_DeleteCollectionNonExisting(self):
        result = DataAPI.DeleteCollection(conn, "C10")
        print("UNIT TEST 37: " + str(result))
        self.assertEqual(result, "Collection C10 does not exist - cannot be deleted")

    #UNIT TEST 38: DELETING A NON EMPTY COLLECTION
    def test_DeleteCollectionNotEmpty(self):
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B16", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.DeleteCollection(conn, "C10")
        print("UNIT TEST 38: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result, "Collection C10 is not empty - cannot be deleted")

    #UNIT TEST 39: ADDING A SAMPLE TEST
    def test_AddSampleTestSuccessful(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        result = DataAPI.AddSampleTest(conn, "S20", "testType", "testResult")
        print("UNIT TEST 39: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Successfully added sample test for sample ID S20")

    #UNIT TEST 40: ADD A SAMPLE TEST TO NON EXISTENT SAMPLE
    def test_AddSampleTestNonExistingSample(self):
        result = DataAPI.AddSampleTest(conn, "S20", "testType", "testResult")
        print("UNIT TEST 40: " + str(result))
        self.assertEqual(result,"Sample ID S20 does not exist - cannot add sample test")

    #UNIT TEST 41: DELETE A SAMPLE TEST
    def test_DeleteSampleTest(self):
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        DataAPI.AddCollection(conn, "C10", "D1", "client1", "1", "1", "1", "1", "1", "1", "1")
        DataAPI.AddSample(conn, "S20", "B10", 1, 1, 1, "BLOOD", "SA", "2020/04/20", "2020/04/20", 20, 0, "C10", "Destroy", "2020/06/20", "Male", "YES")
        DataAPI.AddSampleTest(conn, "S20", "testType", "testResult")
        result = DataAPI.DeleteSampleTest(conn, "S20")
        print("UNIT TEST 41: " + str(result))
        DataAPI.DeleteSample(conn, "S20")
        DataAPI.DeleteCollection(conn, "C10")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Successfully deleted sample test from sample ID S20")

if __name__ == '__main__':
    unittest.main()
    conn.close()

