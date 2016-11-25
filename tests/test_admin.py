#! coding: utf-8
# pylint: disable-msg=W0311
from __future__ import absolute_import, print_function, unicode_literals

import unittest

import six

from pymogile import Admin, MogileFSError


HOST = "testhost"
DOMAIN = "testdomain"
CLASS = "testclass"
TRACKERS = ["127.0.0.1:7001"]


class AdminTest(unittest.TestCase):
  def setUp(self):
    self.mogilefs = Admin(TRACKERS)
    self._delete_classes_and_domains_and_hosts()

  def tearDown(self):
    self._delete_classes_and_domains_and_hosts()

  def _delete_classes_and_domains_and_hosts(self):
    if DOMAIN in self.mogilefs.get_domains():
      if CLASS in self.mogilefs.get_domains()[DOMAIN]:
        self.mogilefs.delete_class(DOMAIN, CLASS)
      self.mogilefs.delete_domain(DOMAIN)
    if any([HOST in host['hostname'] for host in self.mogilefs.get_hosts()]):
      self.mogilefs.delete_host(HOST)

  def test_create_domain(self):
    self.assertEqual(self.mogilefs.create_domain(DOMAIN), True)

  def test_create_and_delete_domain(self):
    self.mogilefs.create_domain(DOMAIN)
    self.assertEqual(self.mogilefs.delete_domain(DOMAIN), True)

  def test_create_existing_domain(self):
    self.mogilefs.create_domain(DOMAIN)
    with self.assertRaises(MogileFSError):
      self.mogilefs.create_domain(DOMAIN)

  def test_create_class(self):
    self.mogilefs.create_domain(DOMAIN)
    self.assertEqual(self.mogilefs.create_class(DOMAIN, CLASS, 2), True)

  def test_create_and_delete_class(self):
    self.mogilefs.create_domain(DOMAIN)
    self.mogilefs.create_class(DOMAIN, CLASS, 2)
    self.assertEqual(self.mogilefs.delete_class(DOMAIN, CLASS), True)

  def test_create_existing_class(self):
    self.mogilefs.create_domain(DOMAIN)
    self.mogilefs.create_class(DOMAIN, CLASS, 2)
    with self.assertRaises(MogileFSError):
      self.mogilefs.create_class(DOMAIN, CLASS, 2)

  def test_get_domains(self):
    self.mogilefs.create_domain(DOMAIN)
    self.mogilefs.create_class(DOMAIN, CLASS, 2)

    ret = self.mogilefs.get_domains()
    assert DOMAIN in ret
    assert CLASS in ret[DOMAIN], ret
    assert ret[DOMAIN][CLASS] == 2, ret

    self.mogilefs.delete_domain(DOMAIN)

  def test_get_server_settings(self):
    res = self.mogilefs.server_settings()
    assert res is not None
    assert 'schema_version' in res

  def test_set_server_setting(self):
    self.mogilefs.set_server_setting("memcache_servers", "127.0.0.1:11211")
    res = self.mogilefs.server_settings()
    assert res['memcache_servers'] == '127.0.0.1:11211'

  def test_get_devices(self):
    devices = self.mogilefs.get_devices()
    assert devices
    for d in devices:
      assert 'devid' in d
      assert 'hostid' in d
      assert 'status' in d
      assert 'observed_state' in d
      assert 'utilization' in d
      assert 'mb_total' in d
      assert 'mb_used' in d
      assert 'weight' in d
      #assert isinstance(d['mb_total'], six.integer_types)
      #assert isinstance(d['mb_used'], six.integer_types)
      #assert isinstance(d['weight'], six.integer_types)

  def test_create_host(self):
    response = self.mogilefs.create_host(HOST, '192.168.0.1', 7500)
    self.assertIsInstance(response, dict)

  def test_create_and_delete_host(self):
    self.mogilefs.create_host(HOST, '192.168.0.1', 7500)
    response = self.mogilefs.delete_host(HOST)
    self.assertEqual(response, True)

#  def test_update_device(self):
#      ## TODO
#      self.mogilefs.update_device('colinux', 1, status='down', weight=80)
#      self.mogilefs.update_device('colinux', 1, status='alive', weight=100)
#
#  def test_change_device_state(self):
#      ## TODO
#      self.mogilefs.change_device_state('colinux', 1, 'down')
#      self.mogilefs.change_device_state('colinux', 1, 'alive')
#
#  def test_change_device_weight(self):
#      ## TODO
#      self.mogilefs.change_device_weight('colinux', 1, 80)
#      self.mogilefs.change_device_weight('colinux', 1, 100)
#
#      try:
#          self.mogilefs.change_device_weight('colinux', 1, "SPAM")
#      except ValueError:
#          pass
#      else:
#          assert False, "ValueError expected for invalid weight"

#  def test_fsck_start(self):
#      self.mogilefs.fsck_start()
#      status = self.mogilefs.fsck_status()
#      assert status['running'] == '1'
#
#      self.mogilefs.fsck_stop()
#      status = self.mogilefs.fsck_status()
#      assert status['running'] == '0'
#
#  def test_fsck_reset(self):
#      self.mogilefs.fsck_reset(0, 0)
#
#  def test_fsck_log_rows(self):
#      self.mogilefs.fsck_log_rows()
#
#  def test_fsck_clearlog(self):
#      self.mogilefs.fsck_clearlog()
#
#  def test_list_fids(self):
#      self.mogilefs.list_fids(1, 10)
#
#  def test_get_stats(self):
#      self.mogilefs.get_stats()
#
#  def test_slave_list(self):
#      assert False
#
#  def test_slave_add(self):
#      assert False
#
#  def test_slave_modify(self):
#      assert False
#
#  def test_slave_delete(self):
#      assert False

if __name__ == "__main__":
  unittest.main()
