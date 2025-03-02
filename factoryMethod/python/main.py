from document_creator import ResumeCreator, ReportCreator

#Cliente que usa el factoryMethod
resumeCreator = ResumeCreator()
reportCreator = ReportCreator()

# Crear y usar un curriculum
print("Creando un curriculum: ")
resume = resumeCreator.do_operation()

print("\nCreando un reporte: ")
report = reportCreator.do_operation()

