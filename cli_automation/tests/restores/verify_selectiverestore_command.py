import unittest
import sys
from time import sleep
sys.path.append("/opt/stack/tempest/cli_automation")
from cliconfig import configuration,command_argument_string
from utils import cli_parser,query_data

class restore_selective_command_test(unittest.TestCase):
    def runTest(self):
        workload_id = query_data.get_workload_id(configuration.workload_name)
        # workload_vm_id = query_data.get_workload_vmid(workload_id)
        # delete_vm_command = command_argument_string + workload_vm_id
        # rc = cli_parser.cli_returncode(delete_vm_command)
        # print rc
        # if rc != 0:
        #     raise Exception("Command did not execute correctly!!!")
        # else:
        #     print ("Command executed correctly!!!")
        snapshot_id = query_data.get_workload_snapshot_id(workload_id)
	print snapshot_id
        restore_command = command_argument_string.selective_restore + " " +snapshot_id
	print restore_command
        rc = cli_parser.cli_returncode(restore_command)
        print rc
        if rc != 0:
            raise Exception("Command did not execute correctly!!!")
        else:
            print ("Command executed correctly!!!")
        wc = query_data.get_snapshot_restore_status(configuration.selective_restore_name,snapshot_id)
        while (str(wc) != "available" or str(wc)!= "error"):
            sleep (5)
            wc = query_data.get_snapshot_restore_status(configuration.selective_restore_name, snapshot_id)
            if (str(wc) == "available"):
                print "Snapshot Restore successfully completed"
                self.created = True
                break
            else:
                if (str(wc) == "error"):
                    break
        if (self.created == False):
            raise Exception ("Snapshot Restore did not get created!!!")


if __name__ == '__main__':
    unittest.main()



