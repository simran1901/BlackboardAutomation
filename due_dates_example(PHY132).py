"""Import python functionality"""
import sys
import time
import pandas as pd
from selenium import webdriver

"""Append Local file locations to to PYTHONPATH"""
sys.path.insert(0, '/Users/andrewadams/Desktop/FunBBAs/LMSA-core/src')

"""Import LMSA functionality"""
from lmsa.manipulation.ASU.ASU_manipulator import ASU_manipulator
from lmsa.lms.blackboard.BlackBoard import Editor
from lmsa.lms.blackboard.content.assignments import Assignments
from lmsa.lms.blackboard.content.folders import Folders
from lmsa.lms.blackboard.Library import Logic
from lmsa.lms.blackboard.Library import Window

"""Global Variables"""
filename = '/Users/andrewadams/Desktop/FunBBAs/LMSA-core/scripts/input/due_dates_template.csv'
prefix1 = '2018Spring-T-PHY122-'
prefix2 = 'PHY 114: General Physics Laboratory (2018 Spring)-'
data = pd.read_csv(filename, dtype=str, delimiter=',', header=None)

"""Initialize WebDriver object"""
driver = webdriver.Chrome('/Users/andrewadams/Desktop/FunBBAs/LMSA-core/scripts/chromedriver_233')

"""Change to FALSE when ready to save changes"""
DRYRUN = False

"""Declare objects"""
institution = ASU_manipulator(driver)
LAB_REPORTS = Assignments(driver)
FORM = Editor(driver)

"""Login"""
"institution.login()"


"""Navigate home"""
Window(driver).home(wait=3)
time.sleep(4)
pause = raw_input('Scroll until desired section is in view\n\nOnce in view press: <ENTER>')
"""Bulk Edit"""
i = 1
for i in range(1, len(data[0])):

    """This pause is a quick fix for elementNotFound error"""
    #pause = raw_input('Scroll until desired section is in view\n\nOnce in view press: <ENTER>')

    """This is the code that finds each section number on the BlackBoard homepage"""
    driver.find_element_by_link_text(prefix1 + str(data[0][i])).click()
    print('Starting Section: ' + str(data[0][i]))

    class test_options:

        OPEN_TEST_IN_NEW_WINDOW_YES = '//*[@id="yesRadio"]'
        OPEN_TEST_IN_NEW_WINDOW_NO = '//*[@id="noRadio"]'
        MAKE_LINK_AVAILABLE_YES = '//*[@id="fIsLinkVisible1"]'
        MAKE_LINK_AVAILABLE_NO = '//*[@id="fIsLinkVisible2"]'
        CREATE_ANNOUNCEMENT_YES = '//*[@id="fCreateAnnouncement1"]'
        CREATE_ANNOUNCEMENT_NO = '//*[@id="fCreateAnnouncement2"]'
        MULTIPLE_ATTEMPTS_CHECK = '//*[@id="fIsMultipleAttempts"]'
        ALLOW_UNLIMITED_ATTEMPTS = '//*[@id="fIsUnlimitedAttempts"]'
        NUMBER_OF_ATTEMPTS = '//*[@id="fNumMultipleAttempts"]'
        NUMBER_OF_ATTEMPTS_VALUE = '//*[@id="attemptCount"]'
        FORCE_COMPLETION_CHECK = '//*[@id="fIsForceComplete"]'
        START_RESTRICT_CHECK = '//*[@id="start_restrict"]'
        START_RESTRICT_DATE = '//*[@id="dp_restrict_start_date"]'
        START_RESTRICT_TIME = '//*[@id="tp_restrict_start_time"]'
        END_RESTRICT_CHECK = '//*[@id="end_restrict"]'
        END_RESTRICT_DATE = '//*[@id="dp_restrict_end_date"]'
        END_RESTRICT_TIME = '//*[@id="tp_restrict_end_time"]'
        DUE_DATE_CHECK = '//*[@id="due_date_in_use"]'
        """DUE_DATE_DATE = '//*[@id="dp_dueDate_date"]'
        DUE_DATE_VALUE = '//*[@id="dp_dueDate_date"]'"""
        DUE_DATE_TIME = '//*[@id="tp_dueDate_time"]'
        LATE_SUBMISSION_CHECK = '//*[@id="doNotAllowLateSubmission"]'

    class assignment_options:

        DUE_DATE_CHECK = '//*[@id="due_date_in_use"]'
        DUE_DATE_VALUE = '//*[@id="dp_dueDate_date"]'
        DUE_DATE_TIME = '//*[@id="tp_dueDate_time"]'
        POINTS_POSSIBLE = '//*[@id="possible"]'
        MAKE_ASSIGNMENT_AVAILABLE = '//*[@id="isAvailable"]'
        START_LIMIT_AVAILABILITY_CHECK = '//*[@id="start_limitAvailability"]'
        START_LIMIT_AVAILABILITY_DATE = '//*[@id="dp_limitAvailability_start_date"]'
        START_LIMIT_AVAILABILITY_TIME = '//*[@id="tp_limitAvailability_start_time"]'
        END_LIMIT_AVAILABILITY_CHECK = '//*[@id="end_limitAvailability"]'
        END_LIMIT_AVAILABILITY_DATE = '//*[@id="dp_limitAvailability_end_date"]'
        END_LIMIT_AVAILABILITY_TIME = '//*[@id="tp_limitAvailability_end_time"]'
        TRACK_NUMBER_OF_VIEWS_CHECK = '//*[@id="isTracked"]'

    class Section(object):

        def __init__(self, name, url):
            self.name = name
            self.url = url

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.name

    class Folders(object):

        def __init__ (self, driver):
            self.driver = driver

        def content_view(self):
            return

        def permit_users_to_view(self):
            return

        def track_number_of_views(self):
            return

        def start_restrict(self, state, date, time):
            """Performs all operations related to the 'Start Restrict Date'. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            """current_state = Logic(self.driver).check_state(folder_options.START_RESTRICT_CHECK)
            if current_state != state:
                Logic(self.driver).set_state(xpath=folder_options.START_RESTRICT_CHECK, dstate=state)"""
            if state:
                self.driver.find_element_by_xpath(folder_options.START_RESTRICT_DATE).clear()
                self.driver.find_element_by_xpath(folder_options.START_RESTRICT_TIME).clear()
                self.driver.find_element_by_xpath(folder_options.START_RESTRICT_TIME).send_keys(time)
                self.driver.find_element_by_xpath(folder_options.START_RESTRICT_DATE).send_keys(date)
            return

        def end_restrict(self, state, date, time):
            """Performs all operations related to the 'End Restrict Date'. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            current_state = Logic(self.driver).check_state(folder_options.END_RESTRICT_CHECK)
            if current_state != state:
                Logic(self.driver).set_state(xpath=folder_options.END_RESTRICT_CHECK, dstate=state)
            if state:
                self.driver.find_element_by_xpath(folder_options.END_RESTRICT_DATE).clear()
                self.driver.find_element_by_xpath(folder_options.END_RESTRICT_TIME).clear()
                self.driver.find_element_by_xpath(folder_options.END_RESTRICT_TIME).send_keys(time)
                self.driver.find_element_by_xpath(folder_options.END_RESTRICT_DATE).send_keys(date)

    class Tests(object):

        def __init__ (self, driver):
            self.driver = driver

        def open_test_in_new_window(self):
            return

        def make_link_available(self):
            return

        def create_announcement(self):
            return

        def multiple_attempts(self):
            return

        def force_completion(self):
            return

        def start_restrict(self, state, date, time):
            """Performs all operations related to the 'Start Restrict Date'. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            current_state = Logic(self.driver).check_state(test_options.START_RESTRICT_CHECK)
            if current_state != state:
                Logic(self.driver).set_state(xpath=test_options.START_RESTRICT_CHECK, dstate=state)
            if state:
                self.driver.find_element_by_xpath(test_options.START_RESTRICT_DATE).clear()
                self.driver.find_element_by_xpath(test_options.START_RESTRICT_TIME).clear()
                self.driver.find_element_by_xpath(test_options.START_RESTRICT_TIME).send_keys(time)
                self.driver.find_element_by_xpath(test_options.START_RESTRICT_DATE).send_keys(date)

        def end_restrict(self, state, date, time):
            """Performs all operations related to the 'End Restrict Date'. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            current_state = Logic(self.driver).check_state(test_options.END_RESTRICT_CHECK)
            if current_state != state:
                Logic(self.driver).set_state(xpath=test_options.END_RESTRICT_CHECK, dstate=state)
            if state:
                self.driver.find_element_by_xpath(test_options.END_RESTRICT_DATE).clear()
                self.driver.find_element_by_xpath(test_options.END_RESTRICT_TIME).clear()
                self.driver.find_element_by_xpath(test_options.END_RESTRICT_TIME).send_keys(time)
                self.driver.find_element_by_xpath(test_options.END_RESTRICT_DATE).send_keys(date)

        def due_date(self, state, date, time):
            """Performs all operations related to Due Dates. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            current_state = Logic(self.driver).check_state(test_options.DUE_DATE_CHECK)
            if current_state != state:
                Logic(self.driver).set_state(xpath=test_options.DUE_DATE_CHECK, dstate=state)
            if state:
                self.driver.find_element_by_xpath(test_options.DUE_DATE_VALUE).clear()
                self.driver.find_element_by_xpath(test_options.DUE_DATE_TIME).clear()
                self.driver.find_element_by_xpath(test_options.DUE_DATE_TIME).send_keys(time)
                self.driver.find_element_by_xpath(test_options.DUE_DATE_VALUE).send_keys(date)

        def late_submission(self):
            return

    class Assignments(object):

        def __init__ (self, driver):
            self.driver = driver

        def due_date(self, state, date, time):
            """Performs all operations related to Due Dates. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            """current_state = Logic(self.driver).check_state('//*[@id="due_date_in_use"]')
            if current_state != state:
                Logic(self.driver).set_state(xpath='//*[@id="due_date_in_use"]', dstate=state)"""
            if state:
                self.driver.find_element_by_xpath(assignment_options.DUE_DATE_VALUE).clear()
                self.driver.find_element_by_xpath(assignment_options.DUE_DATE_TIME).clear()
                self.driver.find_element_by_xpath(assignment_options.DUE_DATE_TIME).send_keys(time)
                self.driver.find_element_by_xpath(assignment_options.DUE_DATE_VALUE).send_keys(date)

        def points_possible(self):
            return

        def start_limit_availability(self, state, date, time):
            """Performs all operations related to the 'Start Limit Availability'. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            current_state = Logic(self.driver).check_state(assignment_options.START_LIMIT_AVAILABILITY_CHECK)
            if current_state != state:
                Logic(self.driver).set_state(xpath=assignment_options.START_LIMIT_AVAILABILITY_CHECK, dstate=state)
            if state:
                self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_DATE).clear()
                self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_TIME).clear()
                self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_TIME).send_keys(time)
                self.driver.find_element_by_xpath(assignment_options.START_LIMIT_AVAILABILITY_DATE).send_keys(date)

        def end_limit_availability(self, state, date, time):
            """Performs all operations related to the 'End Limit Availability'. Order matters when invoking multiple
            'send_key' functions.

            Parameters
            ----------
            state : bool
                The desired state of the checkbox element (True/False)

            date : str
                The literal date value in the format mm/dd/yyyy

            time : str
                The literal time value in the format hh:mm AM/PM

            Returns
            -------
            """
            current_state = Logic(self.driver).check_state(assignment_options.END_LIMIT_AVAILABILITY_CHECK)
            if current_state != state:
                Logic(self.driver).set_state(xpath=assignment_options.END_LIMIT_AVAILABILITY_CHECK, dstate=state)
            if state:
                self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_DATE).clear()
                self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_TIME).clear()
                self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_TIME).send_keys(time)
                self.driver.find_element_by_xpath(assignment_options.END_LIMIT_AVAILABILITY_DATE).send_keys(date)

        def track_number_of_views(self):
            return

    class Editor(Tests, Assignments, Folders):

        def __init__ (self, driver):
            self.driver = driver

        CANCEL = '//*[@id="bottom_submitButtonRow"]/input[1]'
        SUBMIT = '//*[@id="bottom_submitButtonRow""]/input[2]'

        def select_form(self, element, wait=2):
            """Selects the options dropdown menu for blackboard
            form items.

            Parameters
            ----------
            element : str
                User inputed title of form name

            wait : int
                Time to pause for page load to complete. Default is None

            Returns
            -------
            """
            driver.execute_script("return arguments[0].scrollIntoView();",driver.find_element_by_xpath('//*[@title=' + "\"" + element + " item options" + "\"" ']').click())
            """self.driver.find_element_by_xpath('//*[@title=' + "\"" + element + " item options" + "\"" ']').click()"""
            print('     Editing: ' + element)
            if wait is not None:
                time.sleep(wait)

        def edit(self, wait=None):
            self.driver.find_element_by_xpath('//a[@title="Edit"]').click()
            if wait is not None:
                time.sleep(wait)

    class Course(object):

        def __init__(self, name, url, course_id, institute):
            self.sections = dict()
            self.name = name
            self.url = url
            self.course_id = course_id
            self.institute = institute

        def gather_sections(self, html):
            soup = bs4.BeautifulSoup(html, 'html.parser')
            palette = soup.find('ul',{'id':'courseMenuPalette_contents'})
            course_list = palette.find_all('li')
            section_names = [c.find('a').find('span').text for c in course_list]
            section_urls = [urljoin(self.institute.URLS['COURSE_LIST'], c.find('a')['href']) for c in course_list]
            sections = [Section(*x) for x in zip(section_names,section_urls)]
            self.sections.update(dict(zip(section_names,sections)))

        def __str__(self):
            return self.name

        def __repr__(self):
            return self.name

    class Logic(object):

        def __init__ (self, driver):
            self.driver = driver

        def check_state(self, xpath):
            """Checks the state of a given element, returns
            its boolean value.

            Parameters
            ----------
            xpath : str
                Raw xpath formatted as string value. Should be using
                global variable from assignment_options/test_options

            Returns
            -------
            boolean
                Returns 'True' if element is selected, and 'False' otherwise
            """
            x = self.driver.find_element_by_xpath(xpath)
            if x.is_selected() == True:
                return True
            return False

        def set_state(self, xpath, dstate):
            """Sets the desired state of an element.

            Parameters
            ----------
            xpath : str
                Raw xpath formatted as string value. Should be using
                global variable from assignment_options/test_options

            state : bool
                The user's desired state for the given element

            Returns
            -------
            """
            if self.check_state(xpath) != dstate:
                self.driver.find_element_by_xpath(xpath).click()

        def cancel(self, wait=None):
            """Click cancel
            """
            try:
                self.driver.find_element_by_xpath(BB_Editor.CANCEL).click()
                if wait is not None:
                    time.sleep(wait)
            except:
                return False

        def submit(self, wait=None):
            """Click submit
            """
            try:
                self.driver.find_element_by_xpath(FORM.SUBMIT).click()
                if wait is not None:
                    time.sleep(wait)
            except:
                return False

    class Window(object):

        def __init__ (self, driver):
            self.driver = driver

        def home(self, wait=None):
            self.driver.get('https://myasucourses.asu.edu/webapps/portal/execute/tabs/tabAction?tab_tab_group_id=_1_1')
            if wait is not None:
                time.sleep(wait)

        def scroll_page_bottom(self):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        def scroll_into_view(self):
            self.driver.execute_script("document.getElementById('newFile_chooseLocalFile').scrollIntoView(true);")

        def maximize_window(self):
            self.driver.maximize_window()




    """Prelabs"""
    driver.find_element_by_link_text('Submit PreLab').click()
    j = 1
    for j in range(1, 11):
        FORM.select_form(data[j+2][0], wait=3)
        driver.find_element_by_xpath('//a[@title="Edit"]').click()
        Tests(driver).due_date(state=True, date=data[j+2][i], time=data[1][i])
        #form.assignment_due_date(state=True, date=df1[j+4][i], time=df1[3][i])
        if not DRYRUN:
            driver.find_element_by_xpath('//*[@id="bottom_submitButtonRow"]/input[2]').click()

        time.sleep(4)

    """Lab reports"""
    """driver.find_element_by_link_text('Submit Lab Report').click()
    k = 1
    for k in range(1, 4):
        FORM.select_form(data[k+12][0], wait=1)
        driver.find_element_by_xpath('//a[@title="Edit"]').click()
        pause = raw_input('Scroll until desired section is in view\n\nOnce in view press: <ENTER>')
        Assignments(driver).due_date(state=True, date=data[k+12][i], time=data[1][i])
        #form.folder_end_restrict_date(state=True, date=df1[k+14][i], time=df1[4][i])
        if not DRYRUN:
            driver.find_element_by_xpath('//*[@id="bottom_submitButtonRow"]/input[2]').click()
            time.sleep(3)"""

    """Navigate Home"""
    Window(driver).home(wait=3)
    time.sleep(3)
