//Determinar si una matriz es simetrica y transpuesta
#include <iostream>

using namespace std;
int matriz[3][3] ={
				//   0 1 2
			/*0*/	{1,2,3},
			/*1*/	{4,5,6},
			/*2*/	{7,8,9}};
int matrizTrans[3][3];	

void calcularMatrizTranspuesta(){
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			matrizTrans[j][i] = matriz[i][j];
		}
	}
	for(int i=0;i<3;i++){
		for(int j=0;j<3;j++){
			cout<<matrizTrans[i][j]<<" ";
		}
		cout<<endl;
	}
}


bool determinarMatrizSimetrica(){
	bool matrizSimetrica = false;
	/*if len(matriz) == len(matriz[0])
		matrizSimetrica = True*/
	
	return matrizSimetrica;
}
		
int main(){
	calcularMatrizTranspuesta();
}
