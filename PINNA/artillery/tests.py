"""
PINNA
tests.py

Created by Shota Shimazu on 2018/03/11

Copyright (c) 2018 Shota Shimazu All Rights Reserved.

This software is released under the terms of restricted, see LICENSE for detail.
https://hplab.work/pinna-music/pinna-music/blob/master/LICENSE
"""

from django.test import TestCase
from .sender import ArtilleryMail, ArtilleryMassMails



class MailSenderTests(TestCase):
    def setUp(self):
        #Setup run before every test method.
        pass

    def tearDown(self):
        #Clean up run after every test method.
        pass

    def test_something_that_will_pass(self):
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)

    
    def single_mail_send(self):

        mail = ArtilleryMail(
            "pinner@pinna.ml",                  # To
            "from@pinna.ml",                    # From
            "contact@pinna.ml",                 # Reply address
            "Test Mail Subject",                # Email Subject
            "mail.html",                        # Email View Template
        )

    def mass_mail_send(self):
        
        mail = ArtilleryMassMails(
            ["pinner1@pinna.ml", "pinner2@pinna.ml", "pinner3@pinna.ml"], # To
            "from@labbiness.com",               # From
            "contact@labbiness.com",            # Reply address
            "Test Mail Subject",                # Mail Subject
            "mail.html",                        # Email View Template
        )
