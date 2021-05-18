<h2>Motivation</h2>
Basic unit testing for python using pytest

<h2>Setup</h2>
<ul>
<li>install pytest using : pip install -U pytest</li>
<li>write test files that start with test_ e.g. test_utils.py</li>
<li>write assertions inside the test files</li>
<li>invoke the tests using pytest on the project root</li>
</ul>

<h2>points of interest</h2>
<ul>
<li>in case you have few test file and you want to test specific file use : pytest test_file_name </li>
</ul>

<h2>Open issues</h2>
<ul>
<li>currently source and test files reside together. prefered structure is src and test.but then i need to use relative path in the test file and this requires advanced python that currently i did not used ---> this need to be solved</li>
</ul>
