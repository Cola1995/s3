import optparse
op=optparse.OptionParser()
op.add_option('-s','--server',dest='server')
op.add_option('-p','--port',dest='port')
options,args=op.parse_args()
print(options)
print(options.server)
print(args)