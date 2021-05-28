<h2>Motivation</h2>
Basic unit testing for python using pytest

<h2>Setup pytest</h2>
<ul>
<li>install pytest using : pip install -U pytest</li>
<li>write test files with file name that start with test_ and test functions that start with test_ e.g. test_add()</li>
<li>write assertions inside the test files</li>
<li>invoke the tests using pytest on the project root</li>
</ul>

<h2>Setup pytest-regression</h2>
pip install pytest-regressions

<h2>points of interest</h2>
<ul>
<li>in case you have few test files and you want to test specific file use : pytest test_file_name </li>
<li>notice that source files are under src directory and test files are under tests directory. These name are common but arbitraries</li>
<li>__init__.py in src and tests directory make them modules which is required e.g. in test_utils to do : from src.utils </li>
<li>the files for the regression tests are saved in a directory with the same name as the test module check tests/test_utils , do NOT remove this</li>
</ul>


