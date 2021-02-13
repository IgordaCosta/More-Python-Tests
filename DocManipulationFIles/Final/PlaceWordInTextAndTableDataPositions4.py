

import uno
local = uno.getComponentContext()
resolver = local.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local)
context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
document = desktop.loadComponentFromURL("file:///bla.doc", "_blank", 0, ())
cursor = document.Text.createTextCursor()