.. SphinxStart documentation master file, created by
   sphinx-quickstart on Wed Apr 26 10:44:45 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the site made by a newcomer Napacht
=======================================
I'm leaning how to use the tool sphinx, it is interesting.

You can jump to the tables_ paragraph immediately.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Indices and tables
==================

* :ref:`genindex` 
* :ref:`modindex` 
* :ref:`search`   

codes
==================
**the finess function**

`For the Genetic Algorithom`

This is a normal text paragraph. The next paragraph is a code sample::
	
	def fitness_func(self,chrom1,chrom2):
	    interval=[-10.0,10.0]
	    (x,y)=(self.decode(interval,chrom1),self.decode(interval,chrom2))
	    n=lambda x,y:math.sin(math.sqrt(x*x+y*y))**2-0.5
	    d=lambda x,y:(1+0.001*(x*x+y*y))**2
	    func=lambda x,y:0.5-n(x,y)/d(x,y)
	    return func(x,y)

This is a normal text paragraph again.

Footnotes
=====================
Lorem ipsum [1]_ dolor sit amet ... [2]_

.. rubric:: Footnotes

.. [1] Text of the first footnote.
.. [2] Text of the second footnote.

Bullet Lists
======================

- This is the first bullet list item.  The blank line above the
  first list item is required; blank lines between list items
  (such as below this paragraph) are optional.

- This is the first paragraph in the second item in the list.

  This is the second paragraph in the second item in the list.
  The blank line above this paragraph is required.  The left edge
  of this paragraph lines up with the paragraph above, both
  indented relative to the bullet.

  - This is a sublist.  The bullet lines up with the left edge of
    the text blocks above.  A sublist is a new list so requires a
    blank line above and below.

- This is the third item of the main list.

Insert a picture here:

|biohazard|

.. |biohazard| image:: biohazard.png

Field lists
===================

:what: Field lists map field names to field bodies, like
       database records.  They are often part of an extension
       syntax.

:how: The field marker is a colon, the field name, and a
      colon.

      The field body may contain one or more body elements,
      indented relative to the field marker.
	  
Tables
===================

+------------------------+------------+----------+
| Header row, column 1   | Header 2   | Header 3 |
+========================+============+==========+
| body row 1, column 1   | column 2   | column 3 |
+------------------------+------------+----------+
| body row 2             | Cells may span        |
+------------------------+-----------------------+

.. _Tables:

This is a table.

See the Python_ home page for info.

`Write to me`_ with your questions.

.. _Python: http://www.python.org
.. _Write to me: jdoe@example.com
