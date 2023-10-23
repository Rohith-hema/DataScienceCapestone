{
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<center>\n    <img src=\"https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png\" width=\"300\" alt=\"cognitiveclass.ai logo\"  />\n</center>\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "# **Space X  Falcon 9 First Stage Landing Prediction**\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "## Lab 2: Data wrangling\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Estimated time needed: **60** minutes\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "In this lab, we will perform some Exploratory Data Analysis (EDA) to find some patterns in the data and determine what would be the label for training supervised models.\n\nIn the data set, there are several different cases where the booster did not land successfully. Sometimes a landing was attempted but failed due to an accident; for example, <code>True Ocean</code> means the mission outcome was successfully  landed to a specific region of the ocean while <code>False Ocean</code> means the mission outcome was unsuccessfully landed to a specific region of the ocean. <code>True RTLS</code> means the mission outcome was successfully  landed to a ground pad <code>False RTLS</code> means the mission outcome was unsuccessfully landed to a ground pad.<code>True ASDS</code> means the mission outcome was successfully landed on  a drone ship <code>False ASDS</code> means the mission outcome was unsuccessfully landed on a drone ship.\n\nIn this lab we will mainly convert those outcomes into Training Labels with `1` means the booster successfully landed `0` means it was unsuccessful.\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Falcon 9 first stage will land successfully\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/landing\\_1.gif)\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Several examples of an unsuccessful landing are shown here:\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/crash.gif)\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": ""
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "## Objectives\n\nPerform exploratory  Data Analysis and determine Training Labels\n\n*   Exploratory Data Analysis\n*   Determine Training Labels\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "***\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "## Import Libraries and Define Auxiliary Functions\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "We will import the following libraries.\n"
        },
        {
            "cell_type": "code",
            "execution_count": 1,
            "metadata": {},
            "outputs": [],
            "source": "# Pandas is a software library written for the Python programming language for data manipulation and analysis.\nimport pandas as pd\n#NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays\nimport numpy as np"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### Data Analysis\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Load Space X dataset, from last section.\n"
        },
        {
            "cell_type": "code",
            "execution_count": 2,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/html": "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>FlightNumber</th>\n      <th>Date</th>\n      <th>BoosterVersion</th>\n      <th>PayloadMass</th>\n      <th>Orbit</th>\n      <th>LaunchSite</th>\n      <th>Outcome</th>\n      <th>Flights</th>\n      <th>GridFins</th>\n      <th>Reused</th>\n      <th>Legs</th>\n      <th>LandingPad</th>\n      <th>Block</th>\n      <th>ReusedCount</th>\n      <th>Serial</th>\n      <th>Longitude</th>\n      <th>Latitude</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>0</th>\n      <td>1</td>\n      <td>2010-06-04</td>\n      <td>Falcon 9</td>\n      <td>6104.959412</td>\n      <td>LEO</td>\n      <td>CCAFS SLC 40</td>\n      <td>None None</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B0003</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>1</th>\n      <td>2</td>\n      <td>2012-05-22</td>\n      <td>Falcon 9</td>\n      <td>525.000000</td>\n      <td>LEO</td>\n      <td>CCAFS SLC 40</td>\n      <td>None None</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B0005</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>2</th>\n      <td>3</td>\n      <td>2013-03-01</td>\n      <td>Falcon 9</td>\n      <td>677.000000</td>\n      <td>ISS</td>\n      <td>CCAFS SLC 40</td>\n      <td>None None</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B0007</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>3</th>\n      <td>4</td>\n      <td>2013-09-29</td>\n      <td>Falcon 9</td>\n      <td>500.000000</td>\n      <td>PO</td>\n      <td>VAFB SLC 4E</td>\n      <td>False Ocean</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B1003</td>\n      <td>-120.610829</td>\n      <td>34.632093</td>\n    </tr>\n    <tr>\n      <th>4</th>\n      <td>5</td>\n      <td>2013-12-03</td>\n      <td>Falcon 9</td>\n      <td>3170.000000</td>\n      <td>GTO</td>\n      <td>CCAFS SLC 40</td>\n      <td>None None</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B1004</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>5</th>\n      <td>6</td>\n      <td>2014-01-06</td>\n      <td>Falcon 9</td>\n      <td>3325.000000</td>\n      <td>GTO</td>\n      <td>CCAFS SLC 40</td>\n      <td>None None</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B1005</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>6</th>\n      <td>7</td>\n      <td>2014-04-18</td>\n      <td>Falcon 9</td>\n      <td>2296.000000</td>\n      <td>ISS</td>\n      <td>CCAFS SLC 40</td>\n      <td>True Ocean</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>True</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B1006</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>7</th>\n      <td>8</td>\n      <td>2014-07-14</td>\n      <td>Falcon 9</td>\n      <td>1316.000000</td>\n      <td>LEO</td>\n      <td>CCAFS SLC 40</td>\n      <td>True Ocean</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>True</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B1007</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>8</th>\n      <td>9</td>\n      <td>2014-08-05</td>\n      <td>Falcon 9</td>\n      <td>4535.000000</td>\n      <td>GTO</td>\n      <td>CCAFS SLC 40</td>\n      <td>None None</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B1008</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n    <tr>\n      <th>9</th>\n      <td>10</td>\n      <td>2014-09-07</td>\n      <td>Falcon 9</td>\n      <td>4428.000000</td>\n      <td>GTO</td>\n      <td>CCAFS SLC 40</td>\n      <td>None None</td>\n      <td>1</td>\n      <td>False</td>\n      <td>False</td>\n      <td>False</td>\n      <td>NaN</td>\n      <td>1.0</td>\n      <td>0</td>\n      <td>B1011</td>\n      <td>-80.577366</td>\n      <td>28.561857</td>\n    </tr>\n  </tbody>\n</table>\n</div>",
                        "text/plain": "   FlightNumber        Date BoosterVersion  PayloadMass Orbit    LaunchSite  \\\n0             1  2010-06-04       Falcon 9  6104.959412   LEO  CCAFS SLC 40   \n1             2  2012-05-22       Falcon 9   525.000000   LEO  CCAFS SLC 40   \n2             3  2013-03-01       Falcon 9   677.000000   ISS  CCAFS SLC 40   \n3             4  2013-09-29       Falcon 9   500.000000    PO   VAFB SLC 4E   \n4             5  2013-12-03       Falcon 9  3170.000000   GTO  CCAFS SLC 40   \n5             6  2014-01-06       Falcon 9  3325.000000   GTO  CCAFS SLC 40   \n6             7  2014-04-18       Falcon 9  2296.000000   ISS  CCAFS SLC 40   \n7             8  2014-07-14       Falcon 9  1316.000000   LEO  CCAFS SLC 40   \n8             9  2014-08-05       Falcon 9  4535.000000   GTO  CCAFS SLC 40   \n9            10  2014-09-07       Falcon 9  4428.000000   GTO  CCAFS SLC 40   \n\n       Outcome  Flights  GridFins  Reused   Legs LandingPad  Block  \\\n0    None None        1     False   False  False        NaN    1.0   \n1    None None        1     False   False  False        NaN    1.0   \n2    None None        1     False   False  False        NaN    1.0   \n3  False Ocean        1     False   False  False        NaN    1.0   \n4    None None        1     False   False  False        NaN    1.0   \n5    None None        1     False   False  False        NaN    1.0   \n6   True Ocean        1     False   False   True        NaN    1.0   \n7   True Ocean        1     False   False   True        NaN    1.0   \n8    None None        1     False   False  False        NaN    1.0   \n9    None None        1     False   False  False        NaN    1.0   \n\n   ReusedCount Serial   Longitude   Latitude  \n0            0  B0003  -80.577366  28.561857  \n1            0  B0005  -80.577366  28.561857  \n2            0  B0007  -80.577366  28.561857  \n3            0  B1003 -120.610829  34.632093  \n4            0  B1004  -80.577366  28.561857  \n5            0  B1005  -80.577366  28.561857  \n6            0  B1006  -80.577366  28.561857  \n7            0  B1007  -80.577366  28.561857  \n8            0  B1008  -80.577366  28.561857  \n9            0  B1011  -80.577366  28.561857  "
                    },
                    "execution_count": 2,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df=pd.read_csv(\"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv\")\ndf.head(10)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Identify and calculate the percentage of the missing values in each attribute\n"
        },
        {
            "cell_type": "code",
            "execution_count": 3,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "FlightNumber       0.000\nDate               0.000\nBoosterVersion     0.000\nPayloadMass        0.000\nOrbit              0.000\nLaunchSite         0.000\nOutcome            0.000\nFlights            0.000\nGridFins           0.000\nReused             0.000\nLegs               0.000\nLandingPad        40.625\nBlock              0.000\nReusedCount        0.000\nSerial             0.000\nLongitude          0.000\nLatitude           0.000\ndtype: float64"
                    },
                    "execution_count": 3,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df.isnull().sum()/df.count()*100"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Identify which columns are numerical and categorical:\n"
        },
        {
            "cell_type": "code",
            "execution_count": 4,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "FlightNumber        int64\nDate               object\nBoosterVersion     object\nPayloadMass       float64\nOrbit              object\nLaunchSite         object\nOutcome            object\nFlights             int64\nGridFins             bool\nReused               bool\nLegs                 bool\nLandingPad         object\nBlock             float64\nReusedCount         int64\nSerial             object\nLongitude         float64\nLatitude          float64\ndtype: object"
                    },
                    "execution_count": 4,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "df.dtypes"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### TASK 1: Calculate the number of launches on each site\n\nThe data contains several Space X  launch facilities: <a href='https://en.wikipedia.org/wiki/List_of_Cape_Canaveral_and_Merritt_Island_launch_sites?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01'>Cape Canaveral Space</a> Launch Complex 40  <b>VAFB SLC 4E </b> , Vandenberg Air Force Base Space Launch Complex 4E <b>(SLC-4E)</b>, Kennedy Space Center Launch Complex 39A <b>KSC LC 39A </b>.The location of each Launch Is placed in the column <code>LaunchSite</code>\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Next, let's see the number of launches for each site.\n\nUse the method  <code>value_counts()</code> on the column <code>LaunchSite</code> to determine the number of launches  on each site:\n"
        },
        {
            "cell_type": "code",
            "execution_count": 5,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "CCAFS SLC 40    55\nKSC LC 39A      22\nVAFB SLC 4E     13\nName: LaunchSite, dtype: int64"
                    },
                    "execution_count": 5,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "# Apply value_counts() on column LaunchSite\ndf.LaunchSite.value_counts()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Each launch aims to an dedicated orbit, and here are some common orbit types:\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "*   <b>LEO</b>: Low Earth orbit (LEO)is an Earth-centred orbit with an altitude of 2,000 km (1,200 mi) or less (approximately one-third of the radius of Earth),\\[1] or with at least 11.25 periods per day (an orbital period of 128 minutes or less) and an eccentricity less than 0.25.\\[2] Most of the manmade objects in outer space are in LEO <a href='https://en.wikipedia.org/wiki/Low_Earth_orbit?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01'>\\[1]</a>.\n\n*   <b>VLEO</b>: Very Low Earth Orbits (VLEO) can be defined as the orbits with a mean altitude below 450 km. Operating in these orbits can provide a number of benefits to Earth observation spacecraft as the spacecraft operates closer to the observation<a href='https://www.researchgate.net/publication/271499606_Very_Low_Earth_Orbit_mission_concepts_for_Earth_Observation_Benefits_and_challenges?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01'>\\[2]</a>.\n\n*   <b>GTO</b> A geosynchronous orbit is a high Earth orbit that allows satellites to match Earth's rotation. Located at 22,236 miles (35,786 kilometers) above Earth's equator, this position is a valuable spot for monitoring weather, communications and surveillance. Because the satellite orbits at the same speed that the Earth is turning, the satellite seems to stay in place over a single longitude, though it may drift north to south,\u201d NASA wrote on its Earth Observatory website <a  href=\"https://www.space.com/29222-geosynchronous-orbit.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\" >\\[3] </a>.\n\n*   <b>SSO (or SO)</b>: It is a Sun-synchronous orbit  also called a heliosynchronous orbit is a nearly polar orbit around a planet, in which the satellite passes over any given point of the planet's surface at the same local mean solar time <a href=\"https://en.wikipedia.org/wiki/Sun-synchronous_orbit?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\">\\[4] <a>.\n\n*   <b>ES-L1 </b>:At the Lagrange points the gravitational forces of the two large bodies cancel out in such a way that a small object placed in orbit there is in equilibrium relative to the center of mass of the large bodies. L1 is one such point between the sun and the earth <a href=\"https://en.wikipedia.org/wiki/Lagrange_point?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01#L1_point\">\\[5]</a> .\n\n*   <b>HEO</b> A highly elliptical orbit, is an elliptic orbit with high eccentricity, usually referring to one around Earth <a href=\"https://en.wikipedia.org/wiki/Highly_elliptical_orbit?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\">\\[6]</a>.\n\n*   <b> ISS </b> A modular space station (habitable artificial satellite) in low Earth orbit. It is a multinational collaborative project between five participating space agencies: NASA (United States), Roscosmos (Russia), JAXA (Japan), ESA (Europe), and CSA (Canada)<a href=\"https://en.wikipedia.org/wiki/International_Space_Station?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\"> \\[7] </a>\n\n*   <b> MEO </b> Geocentric orbits ranging in altitude from 2,000 km (1,200 mi) to just below geosynchronous orbit at 35,786 kilometers (22,236 mi). Also known as an intermediate circular orbit. These are \"most commonly at 20,200 kilometers (12,600 mi), or 20,650 kilometers (12,830 mi), with an orbital period of 12 hours <a href=\"https://en.wikipedia.org/wiki/List_of_orbits?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\"> \\[8] </a>\n\n*   <b> HEO </b> Geocentric orbits above the altitude of geosynchronous orbit (35,786 km or 22,236 mi) <a href=\"https://en.wikipedia.org/wiki/List_of_orbits?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\"> \\[9] </a>\n\n*   <b> GEO </b> It is a circular geosynchronous orbit 35,786 kilometres (22,236 miles) above Earth's equator and following the direction of Earth's rotation <a href=\"https://en.wikipedia.org/wiki/Geostationary_orbit?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\"> \\[10] </a>\n\n*   <b> PO </b> It is one type of satellites in which a satellite passes above or nearly above both poles of the body being orbited (usually a planet such as the Earth <a href=\"https://en.wikipedia.org/wiki/Polar_orbit?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\"> \\[11] </a>\n\nsome are shown in the following plot:\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/api/Images/Orbits.png)\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### TASK 2: Calculate the number and occurrence of each orbit\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Use the method  <code>.value_counts()</code> to determine the number and occurrence of each orbit in the  column <code>Orbit</code>\n"
        },
        {
            "cell_type": "code",
            "execution_count": 6,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "GTO      27\nISS      21\nVLEO     14\nPO        9\nLEO       7\nSSO       5\nMEO       3\nSO        1\nHEO       1\nGEO       1\nES-L1     1\nName: Orbit, dtype: int64"
                    },
                    "execution_count": 6,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "# Apply value_counts on Orbit column\ndf.Orbit.value_counts()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### TASK 3: Calculate the number and occurence of mission outcome per orbit type\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Use the method  <code>value_counts()</code> to determine the number and occurrence of each orbit in the  column <code>Outcome</code> , then assign it to the variable <code>landing_outcomes</code>:\n"
        },
        {
            "cell_type": "code",
            "execution_count": 11,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "True ASDS      41\nNone None      19\nTrue RTLS      14\nFalse ASDS      6\nTrue Ocean      5\nFalse Ocean     2\nNone ASDS       2\nFalse RTLS      1\nName: Outcome, dtype: int64"
                    },
                    "execution_count": 11,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "# landing_outcomes = values on Outcome column\nlanding_outcomes = df.Outcome.value_counts()\nlanding_outcomes"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<code>True Ocean</code> means the mission outcome was successfully  landed to a specific region of the ocean while <code>False Ocean</code> means the mission outcome was unsuccessfully landed to a specific region of the ocean. <code>True RTLS</code> means the mission outcome was successfully  landed to a ground pad <code>False RTLS</code> means the mission outcome was unsuccessfully landed to a ground pad.<code>True ASDS</code> means the mission outcome was successfully  landed to a drone ship <code>False ASDS</code> means the mission outcome was unsuccessfully landed to a drone ship. <code>None ASDS</code> and <code>None None</code> these represent a failure to land.\n"
        },
        {
            "cell_type": "code",
            "execution_count": 12,
            "metadata": {},
            "outputs": [
                {
                    "name": "stdout",
                    "output_type": "stream",
                    "text": "0 True ASDS\n1 None None\n2 True RTLS\n3 False ASDS\n4 True Ocean\n5 False Ocean\n6 None ASDS\n7 False RTLS\n"
                }
            ],
            "source": "for i,outcome in enumerate(landing_outcomes.keys()):\n    print(i,outcome)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "We create a set of outcomes where the second stage did not land successfully:\n"
        },
        {
            "cell_type": "code",
            "execution_count": 13,
            "metadata": {},
            "outputs": [
                {
                    "data": {
                        "text/plain": "{'False ASDS', 'False Ocean', 'False RTLS', 'None ASDS', 'None None'}"
                    },
                    "execution_count": 13,
                    "metadata": {},
                    "output_type": "execute_result"
                }
            ],
            "source": "bad_outcomes=set(landing_outcomes.keys()[[1,3,5,6,7]])\nbad_outcomes"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "### TASK 4: Create a landing outcome label from Outcome column\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Using the <code>Outcome</code>,  create a list where the element is zero if the corresponding  row  in  <code>Outcome</code> is in the set <code>bad_outcome</code>; otherwise, it's one. Then assign it to the variable <code>landing_class</code>:\n"
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": "# landing_class = 0 if bad_outcome\ndf['Class'] = df['Ou'].apply(lambda x: 'value if condition is met' if x condition else 'value if condition is not met')\n# landing_class = 1 otherwise"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "This variable will represent the classification variable that represents the outcome of each launch. If the value is zero, the  first stage did not land successfully; one means  the first stage landed Successfully\n"
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": "df['Class']=landing_class\ndf[['Class']].head(8)"
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": "df.head(5)"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "We can use the following line of code to determine  the success rate:\n"
        },
        {
            "cell_type": "code",
            "execution_count": null,
            "metadata": {},
            "outputs": [],
            "source": "df[\"Class\"].mean()"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "We can now export it to a CSV for the next section,but to make the answers consistent, in the next lab we will provide data in a pre-selected date range.\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<code>df.to_csv(\"dataset_part\\_2.csv\", index=False)</code>\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "## Authors\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<a href=\"https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\">Joseph Santarcangelo</a> has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "<a href=\"https://www.linkedin.com/in/nayefaboutayoun/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDS0321ENSkillsNetwork26802033-2021-01-01\">Nayef Abou Tayoun</a> is a Data Scientist at IBM and pursuing a Master of Management in Artificial intelligence degree at Queen's University.\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "## Change Log\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "| Date (YYYY-MM-DD) | Version | Changed By | Change Description      |\n| ----------------- | ------- | ---------- | ----------------------- |\n| 2020-09-20        | 1.0     | Joseph     | Modified Multiple Areas |\n| 2020-11-04        | 1.1.    | Nayef      | updating the input data |\n| 2021-05-026       | 1.1.    | Joseph      | updating the input data |\n"
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": "Copyright \u00a9 2021 IBM Corporation. All rights reserved.\n"
        }
    ],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3.8",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.10"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}