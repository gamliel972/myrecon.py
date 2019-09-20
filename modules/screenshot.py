# I don't believe in license.
# You can do whatever you want with this program.

import os
import sys
import subprocess
from colored import fg, bg, attr


class Screenshot:

    def run( self, app ):
        sys.stdout.write( '[+] running mod: screenshots\n' )
        cmd = eval( app.config['screenshot']['command'] )
        os.system( cmd )
        # try:
        #     # print(cmd)
        #     subprocess.Popen( cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL )
        # except Exception as e:
        #     sys.stdout.write( "%s[-] error occurred: %s%s\n" % (fg('red'),e,attr(0)) )


    def getReportDatas( self, app ):
        t_vars = {}
        t_vars['n_screenshots'] = '-'
        d_output = app.d_output + app.config['screenshot']['output_dir']

        if os.path.isdir(d_output):
            cmd = 'find "' + d_output + '" -name "*.png" | wc -l'
            try:
                output = subprocess.check_output( cmd, shell=True ).decode('utf-8')
                t_vars['n_screenshots'] = output
            except Exception as e:
                ex = 1
                # sys.stdout.write( "%s[-] error occurred: %s%s\n" % (fg('red'),e,attr(0)) )

        return t_vars

