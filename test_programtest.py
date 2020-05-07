import unittest
import DataAPI
import sqlite3


class TestData(unittest.TestCase):

    #this actually tests adding a new fridge
    def test_AddExistingFridge(self):
        conn = sqlite3.connect('Test.db')
        #Conn, FridgeID, temparture, numshelves,widthshelves, rate)
        result = DataAPI.AddFridge(conn, "F29", 0, 10, 10, 10)
        print(result)
        DataAPI.DeleteFridge(conn, "F29")
        self.assertEqual(result, "Successfully added Fridge F29")

    #this actually tests adding an existing fridge
    def test_AddSuccessfulFridge(self):
        conn = sqlite3.connect('Test.db')
        #Conn, FridgeID, temparture, numshelves,widthshelves, rate)
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        result = DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        print(result)
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result, "Successfully added Fridge F20")

    def test_AddSuccessfulBox(self):
        conn = sqlite3.connect('Test.db')
        DataAPI.AddFridge(conn, "F30", 0, 10, 10, 10)
        #AddBox(_conn, _boxID, _fridgeID, _fridgeX, _fridgeY, _boxX, _boxY, _boxZ)
        result = DataAPI.AddBox(conn, "B30", "F20", 1, 2, 10, 10, 10)
        print(result)
        DataAPI.DeleteBox(conn, "B30")
        DataAPI.DeleteFridge(conn, "F30")
        self.assertEqual(result,"Successfully added Box B30")

    def test_AddboxWrongPosition(self):
        conn = sqlite3.connect('Test.db')
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        #AddBox(_conn, _boxID, _fridgeID, _fridgeX, _fridgeY, _boxX, _boxY, _boxZ)
        DataAPI.AddBox(conn, "B12", "F20", 1, 1, 1, 1, 1)
        result = DataAPI.AddBox(conn, "B11", "F20", 1, 1, 1, 1, 1)
        print(result)
        DataAPI.DeleteBox(conn, "B12")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertNotEqual(result,"Successfully added Box B11")

    def test_AddSampleSuccessful(self):
        conn = sqlite3.connect('Test.db')
        DataAPI.AddFridge(conn, "F20", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B10", "F20", 1, 1, 10, 10, 10)
        # def AddSample(_conn, _sampleID, _boxID, _boxX, _boxY, _boxZ, _sampleType, _originCountry, _collectionDate, _entryDate, _subjectAge, _tubeRating, _collectionTitle, _returnType, _returnDate, _phenotypeValue, _diseaseState):
        result = DataAPI.AddSample(conn, "S20", "B11", 1, 1, 1, "BLOOD", "South Africa", "2020/04/20", "2020/04/20", 20, 0, "C1", "Destroy", "2020/06/20", "Male", "YES")
        DataAPI.DeleteSample(conn, "S20")        
        DataAPI.DeleteBox(conn, "B10")
        DataAPI.DeleteFridge(conn, "F20")
        self.assertEqual(result,"Successfully added sample S20")

    def test_DeleteBox(self):
        conn = sqlite3.connect('Test.db')
        DataAPI.AddFridge(conn, "F21", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B15", "F21", 1, 2, 10, 10, 10)
        result = DataAPI.DeleteBox(conn, "B15")
        DataAPI.DeleteFridge(conn, "F21")
        self.assertEqual(result,"Box: B15 succesfully deleted!")

    def test_MoveBox(self):
        conn = sqlite3.connect('Test.db')
        DataAPI.AddFridge(conn, "F22", 0, 10, 10, 10)
        DataAPI.AddBox(conn, "B16", "F22", 1, 2, 10, 10, 10)
        DataAPI.AddFridge(conn, "F23", 0, 10, 10, 10)
        #MoveBox(_conn, _boxID, _fridgeID, _fridgeX, _fridgeY)
        result = DataAPI.MoveBox(conn, "B16", "F23", 1,2)
        DataAPI.DeleteBox(conn, "B16")
        DataAPI.DeleteFridge(conn, "F23")
        DataAPI.DeleteFridge(conn, "F22")
        self.assertEqual(result,"Box: B16 was moved to fridge: F23 (1,2)")
 


if __name__ == '__main__':
    unittest.main()
