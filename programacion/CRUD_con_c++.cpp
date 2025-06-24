#include <iostream>
#include <vector>
#include <algorithm>
#include <clocale>

using namespace std;

void mostrarVector(vector<int> v, string titulo){
	setlocale(LC_ALL, "es_MX.UFT-8");
	cout<<"\n"<<titulo<<": ";
	if(v.empty()){
		cout<<"Arreglo vacio";
	}else{
		for(const auto& elemento:v){
			cout<<elemento<<" ";
		}
	}
	cout<<"| Tamaño es: "<<v.size()<<endl;
}

int main(){
	setlocale(LC_ALL, "es_MX.UFT-8");
	cout<<"Practica metodos ventor"<<endl;
	cout<<"Creacion del vector "<<endl;
	vector<int> numeros;
	cout<<"Vector creado: "<<(numeros.empty() ? "si":"no")<<endl;
	
	cout<<"Tamaño inicial: "<<numeros.size();
	cout<<".Agregare elementos con push_back"<<endl;
	numeros.push_back(10);
	numeros.push_back(20);
	numeros.push_back(30);
	numeros.push_back(40);
	numeros.push_back(50);
	
	mostrarVector(numeros, "Despues del push_back");
	
	cout<<"\nAcceso a los elementos"<<endl;
	cout<<"Primer elemento con front: "<<numeros.front()<<endl;
	cout<<"Primer elemento con back: "<<numeros.back()<<endl;
	cout<<"Elemento en posicion 2 con []: "<<numeros[2]<<endl;
	cout<<"Elemento en posicion 2 con at: "<<numeros.at(3)<<endl;
	
	cout<<"Acceso a elementos"<<endl;
	numeros[1] = 99;
	numeros.at(3) = 77;
	mostrarVector(numeros, "Despues de modificar elementos");
	
	cout<<"He recorrido con iteradores normales"<<endl
		<<"Recorrido normal(begin->end): ";
	for(auto it = numeros.begin(); it != numeros.end(); it++){//con it desferencio
		cout<<*it<<" ";
	}
	cout<<endl;
	cout<<"Recorrido reverso(rbegin->rend)";
	for(auto it = numeros.rbegin(); it != numeros.rend(); it++){//con it desferencio
		cout<<*it<<" ";
	}
	
	cout<<"\nInsertas elementos "<<endl;
	auto it = numeros.begin() + 2;
	numeros.insert(it,888);
	mostrarVector(numeros, "Despues de insert en posicion 2");
	cout<<endl;
	
	cout<<"\nEliminar ultimo elemento"<<endl;
	cout<<"Ultimo elemento anters del pop_back(): "<<numeros.back()<<endl;
	numeros.pop_back();
	mostrarVector(numeros, "Despues del pop_back");
	
	cout<<"\nEliminar un elemento en especifico"<<endl;
	it = numeros.begin() + 1;
	cout<<"Eliminando elemento en posicion 1: "<<*it<<endl;
	numeros.erase(it);
	mostrarVector(numeros, "Despues de erase");
	
	cout<<"\nBuscar elementos"<<endl;
	auto encontrado = find(numeros.begin(), numeros.end(),888);
	if(encontrado != numeros.end()){
		cout<<"Elemento encontrado en posicion "<<(encontrado - numeros.begin())<<endl;
	}else{
		cout<<"Elemento no encontrado"<<endl;
	}
	
	return 0;
}
