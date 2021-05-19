<h2>Motivation</h2>
Basic unit testing for python using pytest

<h2>Setup</h2>
<ul>
<li>install pytest using : pip install -U pytest</li>
<li>write test files with file name that start with test_ and test functions that start with test_ e.g. test_add()</li>
<li>write assertions inside the test files</li>
<li>invoke the tests using pytest on the project root</li>
</ul>

<h2>points of interest</h2>
<ul>
<li>in case you have few test files and you want to test specific file use : pytest test_file_name </li>
<li>notice that source files are under src directory and test files are under tests directory. These name are common but arbitraries</li>
<li>altough conftest.py is empty it allows pytest to work with the tree directory of src and tests</li>
</ul>


