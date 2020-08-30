import os
import pytest
import logging
import subprocess
import xlrd
import math

from errorHandler import *
from findCPcore   import *

LOGGER = logging.getLogger(__name__)

TEST_MODEL           = "data/MODEL1108160000_url.xml"
INCORRECTLY_FORMATED = "data/incorrectly_formatted.xml"
FINDCPCLI_PATH       = os.path.abspath("../scripts/findCPcli")

def __equal_cell(val1, val2):
    if isinstance(val1, float):
        if math.isnan(val1) and math.isnan(val2):
            return True
        else:
            return math.isclose(val1, val2, rel_tol=1e-5)
    else:
        return val1 == val2

def __compare_two_spreadsheets_content(file1, file2):
    xls1 = xlrd.open_workbook(file1, on_demand=True)
    xls2 = xlrd.open_workbook(file1, on_demand=True)

    i = 0
    for name in xls1.sheet_names():
        sheet1 = xls1.sheet_by_name(name)
        sheet2 = xls2.sheet_by_name(name)
        LOGGER.info("Checking sheet : (col:{},row:{}) {} ".format(sheet1.ncols, sheet1.nrows, name))

        for col in range(sheet1.ncols):
            for row in range(sheet1.nrows):
                val1 = sheet1.cell_value(row, col)
                val2 = sheet2.cell_value(row, col)
                if not __equal_cell(val1, val2):
                    raise CellsNotEqualException(name, row, col, file1, val1, file2, val2)


"""
    Assure script can be runned.
    Test with no args -> informative text expected
"""
def test_no_args():
    
    LOGGER.info("Executing cli file: {}" \
                .format(FINDCPCLI_PATH))

    f = open("data/no_args_err.txt", "r")
    expected_result = f.read()
    f.close()

    try:
        result = subprocess.check_output(['python', FINDCPCLI_PATH], stderr=subprocess.STDOUT, text=True)
        raise RuntimeError("This point should not be reached. Return code must not be 0.")
    except subprocess.CalledProcessError as err:
        assert(str(err.stdout) == expected_result)


"""
    Check error output when passing incorrect sbml input
"""
def test_incorrect_input_model():
    params  = ["-i", INCORRECTLY_FORMATED, "-o", "test_spreadsheet.xls"]

    LOGGER.info("Executing cli file: {} {}" \
                .format(FINDCPCLI_PATH, params))

    f = open("data/test_incorrect_input_model.txt", "r")
    expected_result = f.read()
    f.close()

    result = subprocess.check_output(['python', FINDCPCLI_PATH] + params, \
            stderr=subprocess.STDOUT, \
            text=True)
    assert(str(result) == expected_result)


"""
    Assure correct output and no errors running correct model
"""
#@pytest.mark.skip(reason="")
def test_verbose_output_on_model():
    params  = ["-i", TEST_MODEL, "-o", "test_spreadsheet.xls", "-v"]

    LOGGER.info("Executing cli file: {} {}" \
                .format(FINDCPCLI_PATH, params))

    f = open("data/test_verbose_output_on_model.txt", "r")
    expected_result = f.read()
    f.close()

    result = subprocess.check_output(['python', FINDCPCLI_PATH] + params, \
            stderr=subprocess.STDOUT, \
            text=True)

    assert(str(result) == expected_result)

    LOGGER.info("Comparing spreadsheets: '{}' : '{}'".format( \
        "test_spreadsheet.xls", \
        "data/MODEL1108160000_url.xls" \
    ))

    __compare_two_spreadsheets_content( \
        "test_spreadsheet.xls", \
        "data/MODEL1108160000_url.xls" \
    )


"""
    Assure correct output and no errors running correct model
"""
def test_verbose_chokepoint_computation_on_model():
    params  = ["-i", TEST_MODEL, "-cp", "test_spreadsheet_cp.xls", "-v"]

    LOGGER.info("Executing cli file: {} {}" \
                .format(FINDCPCLI_PATH, params))

    f = open("data/test_verbose_chokepoint_computation_on_model.txt", "r")
    expected_result = f.read()
    f.close()

    result = subprocess.check_output(['python', FINDCPCLI_PATH] + params, \
            stderr=subprocess.STDOUT, \
            text=True)

    assert(str(result) == expected_result)

    LOGGER.info("Comparing spreadsheets: '{}' : '{}'".format( \
        "test_spreadsheet_cp.xls", \
        "data/MODEL1108160000_url_cp.xls" \
    ))

    __compare_two_spreadsheets_content( \
        "test_spreadsheet_cp.xls", \
        "data/MODEL1108160000_url_cp.xls" \
    )


"""
    Assure correct output and no errors generating new models
"""
def test_verbose_generate_new_models():
    params  = ["-i", TEST_MODEL, \
               "-swD",  "model_without_dem.xml", \
               "-sF",   "model_fva_flux.json", \
               "-swDF", "model_fva_dem.yml"]

    LOGGER.info("Executing cli file: {} {}" \
                .format(FINDCPCLI_PATH, params))

    f = open("data/test_verbose_generate_new_models.txt", "r")
    expected_result = f.read()
    f.close()

    result = subprocess.check_output(['python', FINDCPCLI_PATH] + params, \
            stderr=subprocess.STDOUT, \
            text=True)

    assert(str(result) == expected_result)

    #model1 = CobraMetabolicModel("model_without_dem.xml")
    #model1.find_dem()
    #for compartment in model1.dem():
    #    assert(len(model.dem()[compartment]) == 0)

    model2 = CobraMetabolicModel("model_fva_dem.yml")
    model2.find_dem()
    for compartment in model2.dem():
        assert(len(model2.dem()[compartment]) == 0)
