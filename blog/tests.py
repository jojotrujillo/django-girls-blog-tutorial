import unittest
from blog.selenium_tests import test_admin_site, test_add_post

admin_site = unittest.TestLoader().loadTestsFromTestCase(test_admin_site.TestAdminSite)
add_post = unittest.TestLoader().loadTestsFromTestCase(test_add_post.TestAddPost)

test_suite = unittest.TestSuite([admin_site, add_post])

unittest.TextTestRunner(verbosity=2).run(test_suite)
