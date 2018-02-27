from mbed_cloud.subscribe import SubscriptionsManager
from mbed_cloud.subscribe import channels

from tests.common import BaseCase

import mock
import os
import unittest


class Test(BaseCase):
    def test_subscribe(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer_a = subs.subscribe(channels.DeviceStateChanges(device_id='A'))
        observer_b = subs.subscribe(channels.DeviceStateChanges(device_id='B'))
        observer_c = subs.subscribe(channels.DeviceStateChanges())

        self.assertIsNot(observer_a, observer_b)
        self.assertIsNot(observer_b, observer_c)

        future_a = observer_a.next().defer()
        future_b = observer_b.next().defer()
        future_c = observer_c.next().defer()

        self.assertIsNot(future_a, future_b)
        self.assertIsNot(future_b, future_c)

        # an irrelevant channel
        subs.notify({
            channels._API_CHANNELS.async_responses: [
                dict(a=1, b=2, device_id='A')
            ]
        })
        result = future_a.wait(timeout=0.01)
        self.assertFalse(future_a.ready())
        self.assertFalse(future_b.ready())
        self.assertFalse(future_c.ready())

        subs.notify({
            channels._API_CHANNELS.reg_updates: [
                dict(a=1, b=2, device_id='A')
            ]
        })
        result = future_a.get(timeout=2)
        self.assertDictContainsSubset(dict(a=1, b=2), result)

        self.assertFalse(future_b.ready())

        self.assertTrue(future_c.ready())
        result = future_c.get()
        self.assertDictContainsSubset(dict(a=1, b=2), result)

    def test_subscribe_conflict(self):
        subs = SubscriptionsManager(mock.MagicMock())
        observer_a = subs.subscribe(channels.ResourceValueCurrent(device_id='A', resource_path=5))
        observer_b = subs.subscribe(channels.ResourceValueCurrent(device_id='B', resource_path=5))
        observer_c = subs.subscribe(channels.ResourceValueCurrent(device_id='A', resource_path=2))

        subs.notify({
            channels._API_CHANNELS.async_responses: [
                dict(a=1, b=2, device_id='A', resource_path=2)
            ]
        })

        result = observer_c.next().defer().get(timeout=2)
        self.assertDictContainsSubset(dict(a=1, b=2), result)
        self.assertDictContainsSubset(dict(a=1, b=2), result)

    @unittest.skipIf(os.environ.get('CI'), 'Not strictly a unittest')
    def test_live(self):
        from mbed_cloud.connect import ConnectAPI
        api = ConnectAPI()
        d = api.list_connected_devices().first()
        r = api.subscribe(api.subscribe.channels.ResourceValueCurrent(
            device_id=d.id,
            resource_path='/3/0/18',
        )).next().block(timeout=1)
        self.assertTrue(r)

    @unittest.skipIf(os.environ.get('CI'), 'Not strictly a unittest')
    def test_a_live2(self):
        from mbed_cloud.connect import ConnectAPI
        api = ConnectAPI()
        d = api.list_connected_devices().first()
        print('using device', d.id)
        r = api.subscribe(api.subscribe.channels.DeviceStateChanges(device_id=d.id)).next().block(timeout=1)
        print(r)
        self.assertTrue(r)
