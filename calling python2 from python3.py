import execnet
import subprocess

# Answer #1:
def call_python_version(Version, Module, Function, ArgumentList):
    gw      = execnet.makegateway("popen//python=python%s" % Version)
    channel = gw.remote_exec("""
        from %s import %s as the_function
        channel.send(the_function(*channel.receive()))
    """ % (Module, Function))
    channel.send(ArgumentList)
    return channel.receive()



"""
call_python_version("2.7", "FILENAME", "FUNCTION",
                                             [FUNCTION INPUT]
"""
"""protein_sequence = call_python_version("2.7", "uniprot_to_sequence", "protein_uniprot_to_sequence",
                                             [uniprot])"""
#print("protein sequence ",protein_sequence)


#Answer #2:
def method_2():
    import subprocess
    uniprot="P42680"

    script = ["python2.7", "uniprot_to_sequence.py", uniprot]
    process = subprocess.Popen(" ".join(script),
                                            shell=True,
                                            env={"PYTHONPATH": "."})
    output, error = process.communicate()
    print(output)

def method_3(uniprot):
    output=subprocess.check_output(f"python2 uniprot_to_sequence.py U {uniprot}",
                            shell=True)
    print(output.decode('ascii')) # to remove b' and \n'
    return output.decode('ascii')
method_3("P42680")