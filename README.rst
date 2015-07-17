py-Goldsberry
=============

A Python Package for easily acquiring NBA Data for analysis

What is py-Goldsberry and why was it built?
-------------------------------------------

I attended the 2015 Sloan Sports Analytics conference and had the
fortunate opportunity to listen to Kirk Goldsberry
([@kirkgoldsberry](http://twitter.com/kirkgoldsberry)) address the crowd
regarding the state of analytics in sports (You can watch the talk
`here`_). One of the questions he addressed at the end was related to
the availability of data (or lack thereof in some instances). Basically,
he concluded that the lack of availability of some of the newest data is
actually hindering the progression of analytics in sports. Innovation is
now restricted to those with access to data instead of to the entire
community of interested parties. I wrote (am writing) this package in an
attempt to help address this issue in whatever small way I can.

``py-Goldsberry`` is designed to give the user easy access to data
available from stats.nba.com in a form that facilitates innovative
analysis. With a few simple commands, you can have access to virtually
any data available on the site in an easy to analyze format. In fact,
some of the data is in a less summarize form giving you the opportunity
to work with the most raw data possible when you are attempting to
answer questions that interest you.

This package is a work in progress. As the NBA continues to make more
data available, I will do my best to update ``py-Goldsberry`` to reflect
these additions. Currently, there is almost a cumbersome amount of data
available from the NBA so dealing with what is there is a bit of a
challenge.

Getting started
---------------

To get started with ``py-Goldsberry``, you need to install and load the
package. From your terminal, run the following command:

::

    pip install py-goldsberry

Once you have the package installed, you can load it into a Python
session with the following command:

.. code:: python

    import goldsberry
    import pandas as pd

The package is designed to work with `pandas`_ in that the output of
each API call to the NBA website it returned in a format that is easily
converted into a pandas dataframe.

Getting a List of Players
~~~~~~~~~~~~~~~~~~~~~~~~~

One of the key variables necessary to fully utilize ``py-Goldsberry`` is
``playerid``. This is the unique id number assigned to each player by
the NBA. ``py-Goldsberry`` has a top-level function ``PlayerList()``
built-in to give you quick access to a list of players and numbers. When
you run the function, you should specify the year of the season from
which you want the list of available players.

.. code:: python


    playersCurrent = pd.DataFrame(goldsberry.PlayerList(2014))
    playersCurrent.head()

If you want a list of every player in the history of the NBA, you can
pass the ``AllTime=True`` argument:

.. code:: python

    playersAllTime = pd.DataFrame(goldsberry.PlayerList(AllTime=True))
    playersAllTime.head()

.. _here: https://www.youtube.com/watch?v=wLf2hLHlFI8
.. _pandas: http://pandas.pydata.org/