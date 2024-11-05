icmp\_receiver module
=====================

.. automodule:: icmp_receiver
   :members:
   :undoc-members:
   :show-inheritance:

Source Code
-----------

.. literalinclude:: ../receiver/icmp_receiver.py
   :language: python
   :linenos:

Expected Output
-----------
.. code-block:: text

   Listening for ICMP packets:
   Received ICMP:
   ###[ Ethernet ]###
     dst       = 02:42:ac:13:00:03
     src       = 02:42:ac:13:00:02
     type      = IPv4
   ###[ IP ]###
        version   = 4
        ihl       = 5
        tos       = 0x0
        len       = 28
        id        = 1
        flags     =
        frag      = 0
        ttl       = 1
        proto     = icmp
        chksum    = 0x61b5
        src       = 172.19.0.2
        dst       = 172.19.0.3
        \options   \
   ###[ ICMP ]###
          type      = echo-request
          code      = 0
          chksum    = 0xf7ff
          id        = 0x0
          seq       = 0x0
          unused    = b''