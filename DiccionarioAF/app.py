import Factory.AbstractFactory as AF

#RAE productos

RAE = AF.ConcreteFactoryRAE()
prod1 = RAE.Significado()
prod1.Mostrar()
prod2 = RAE.Sinonimo()
prod2.Mostrar()
prod3 = RAE.Antonimo()
prod3.Mostrar()

#WIKIPEDIA productos

Wiki = AF.ConcreteFactoryWiki()
prod1 = Wiki.Significado()
prod1.Mostrar()
prod2 = Wiki.Sinonimo()
prod2.Mostrar()
prod3 = Wiki.Antonimo()
prod3.Mostrar()