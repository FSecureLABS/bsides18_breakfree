# BSidesNYC 2018: I Want to Break Free - Examples

This repository contains the demonstration code and examples used during the talk.

## message.dll

This is a DLL file created using msfvenom whose sole purpose is to display a message box.

```
$ msfvenom -p windows/messagebox -f dll -o message.dll TITLE=BSidesNYC ICON=INFORMATION TEXT="BSidesNYC 2018!"
```

## message.exe

This is an EXE file created using msfvenom whose sole purpose is to display a message box.

```
$ msfvenom -p windows/messagebox -f exe -o message.exe TITLE=BSidesNYC ICON=INFORMATION TEXT="BSidesNYC 2018!"
```

## message.cs

This is a file containing shellcode in a buffer (C style) which displays a message box.

```
$ msfvenom -p windows/messagebox -f csharp -o message.cs TITLE=BSidesNYC ICON=INFORMATION TEXT="BSidesNYC 2018!"
```

## msbuild-message.xml

This is an XML file which, when run with msbuild.exe, will run inline shellcode. It was originally developed by
Casey Smith (@subTee), but the shellcode has been replaced by the output of message.cs (above).

## file2vb.py

This is a python script which takes a file as a parameter and:
1. Converts it to a character-by-character chr() representation
2. Splits it up into multiple functions if it would end up being too large
3. Formats it so that it can be copy/pasted into a VB macro

Note that this a proof of concept script; there are many ways it can be improved; ideas include:
1. Using an array rather than a chr() concatenation
2. Stripping of unnecessary whitespace or other characters
3. Base64 encoding or compression
4. Obfuscation of some description

## BSidesNYC_Message.doc

This is an example word document containing a macro which, when executed, will drop an XML file to disk and
run it using msbuild.exe. This is to demonstrate a method of bypassing default AppLocker rules without calling
PowerShell.

As discussed during the talk, it does have some disadvantages (e.g. execution of a separate binary, dropping
a file to disk), but in itself works well as a proof of concept to demonstrate an alternative method of 
executing an implant.
