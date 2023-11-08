#include"trajobjfuns.h"
#include<vector>
#include<iostream>

int main(int argc, char* argv[]){
	using namespace std;

	if(argc != 5){
		cerr << "Wrong number of parameters" << endl;
		return 1;
	}

	//Put here your solution
	vector<double> X(4);
	for(int i = 1; i < argc; i++)
		X[i-1] = stold(argv[i]);
	vector<double> vp;
	
	double obj = jupiter2(X,vp);

	//Printing the point
	// cout << "X = [";
	// for(int i = 0; i < X.size() - 1; i++)
	// 	cout << X[i] << ", ";
	// cout << X.back() << "]\n";

	
	//Printing the result:
	cout << obj << endl;

	return 0;
}
