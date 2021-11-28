import argparse

from core.monitor_dbs_simulator import Monitor_DBS_simulator
from core.monitor_ims_simulator import Monitor_IMS_simulator
from core.peer_dbs import Peer_DBS
from core.peer_dbs_simulator import Peer_DBS_simulator
from monitor import Monitor


class Monitor_simulator(Monitor):

    def add_args(self, parser):
        super().add_args(parser)
        parser.add_argument("-l", "--chunks_before_leave", default=Peer_DBS_simulator.chunks_before_leave, type=int,
                            help="Number of chunk before leave the team (default={})"
                            .format(Peer_DBS_simulator.chunks_before_leave))

    def instance(self, args):
        Peer_DBS.peer_port = int(args.peer_port)
        Peer_DBS.splitter = (args.splitter_address, int(args.splitter_port))
        Peer_DBS_simulator.chunks_before_leave = int(args.chunks_before_leave)
        if args.set_of_rules == "DBS":
            self.peer = Monitor_DBS_simulator("P", "Monitor_DBS_simulator", args.loglevel)
        else:
            self.peer = Monitor_IMS_simulator("P", "Monitor_IMS_simulator", args.loglevel)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    peer = Monitor_simulator()
    peer.add_args(parser)
    args = parser.parse_args()
    peer.instance(args)
    peer.run(args)
