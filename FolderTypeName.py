



InnerFolderName0 = str('''PC  b<><c\\c2\\d//e||f::g**h??j<<k>>l""m''''')


InnerFolderName1 = InnerFolderName0.replace(' ', '_').replace('\\', '_').replace('/', '_').replace('|', '_').replace(':', '_').replace('*', '_').replace('?', '_').replace('>', '_').replace('<', '_').replace('"', '_').replace("'", '_')

InnerFolderName = InnerFolderName1 + '\\'



print(InnerFolderName)
