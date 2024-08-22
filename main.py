# main.py

import numpy as np
from constants import FUNC_CONVEX, FUNC_NCONVEX,NAME_CONVEX,NAME_NCONVEX, PROBLEM_DICT_CONVEX10, PROBLEM_DICT_NCONVEX10, PROBLEM_DICT_CONVEX, PROBLEM_DICT_NCONVEX, TERM_DICT
from cases import TrabCases
from plotting import plot_heatmap_with_points, plot_heatmap_with_points_testCase

# Create and run test cases for convex and non-convex functions
def run_test_cases():
    cases10dim1 = TrabCases()
    for _ in range(10):
        cases10dim1.randomWithOnepoint(problem_dict=PROBLEM_DICT_CONVEX10)
        cases10dim1.tournamentWithOnepoint(problem_dict=PROBLEM_DICT_CONVEX10)
        cases10dim1.randomWithMultipoints(problem_dict=PROBLEM_DICT_CONVEX10)
        cases10dim1.tournamentWithMultipoints(problem_dict=PROBLEM_DICT_CONVEX10)
    cases10dim1.npArray()

    cases10dim2 = TrabCases()
    for _ in range(10):
        cases10dim2.randomWithOnepoint(problem_dict=PROBLEM_DICT_NCONVEX10)
        cases10dim2.tournamentWithOnepoint(problem_dict=PROBLEM_DICT_NCONVEX10)
        cases10dim2.randomWithMultipoints(problem_dict=PROBLEM_DICT_NCONVEX10)
        cases10dim2.tournamentWithMultipoints(problem_dict=PROBLEM_DICT_NCONVEX10)
    cases10dim2.npArray()

    cases2dim1 = TrabCases()
    for _ in range(10):
        cases2dim1.randomWithOnepoint(problem_dict=PROBLEM_DICT_CONVEX)
        cases2dim1.tournamentWithOnepoint(problem_dict=PROBLEM_DICT_CONVEX)
        cases2dim1.randomWithMultipoints(problem_dict=PROBLEM_DICT_CONVEX)
        cases2dim1.tournamentWithMultipoints(problem_dict=PROBLEM_DICT_CONVEX)
    cases2dim1.npArray()

    cases2dim2 = TrabCases()
    for _ in range(10):
        cases2dim2.randomWithOnepoint(problem_dict=PROBLEM_DICT_NCONVEX)
        cases2dim2.tournamentWithOnepoint(problem_dict=PROBLEM_DICT_NCONVEX)
        cases2dim2.randomWithMultipoints(problem_dict=PROBLEM_DICT_NCONVEX)
        cases2dim2.tournamentWithMultipoints(problem_dict=PROBLEM_DICT_NCONVEX)
    cases2dim2.npArray()
    
    # Print results
    def print_results(cases, description):
        print(f"============== {description} ==============")
        print("Randomico com um ponto:")
        print("Média fitness de 10 iteracoes: " + str(np.sum(cases.randomWithOnepointFitness) / 10))
        print("Melhor fitness de 10 iteracoes: " + str(np.min(cases.randomWithOnepointFitness)))

        print("Torneio com um ponto:")
        print("Média fitness de 10 iteracoes: " + str(np.sum(cases.tournamentWithOnepointFitness) / 10))
        print("Melhor fitness de 10 iteracoes: " + str(np.min(cases.randomWithOnepointFitness)))

        print("Randomico com multiplos pontos:")
        print("Média fitness de 10 iteracoes: " + str(np.sum(cases.randomWithMultipointsFitness) / 10))
        print("Melhor fitness de 10 iteracoes: " + str(np.min(cases.randomWithOnepointFitness)))

        print("Torneio com multiplos pontos:")
        print("Média fitness de 10 iteracoes: " + str(np.sum(cases.tournamentWithMultipointsFitness) / 10))
        print("Melhor fitness de 10 iteracoes: " + str(np.min(cases.randomWithOnepointFitness)))
        print("==========================================")

    print_results(cases10dim1, "Casos Convexo e 10 dimensões")
    print_results(cases10dim2, "Casos não Convexo e 10 dimensões")
    print_results(cases2dim1, "Casos Convexo e 2 dimensões")
    print_results(cases2dim2, "Casos não Convexo e 2 dimensões")

    # Plot heatmaps
    plot_heatmap_with_points(func=FUNC_CONVEX, cases=cases2dim1,name = NAME_CONVEX)
    plot_heatmap_with_points(func=FUNC_NCONVEX, cases=cases2dim2,name = NAME_NCONVEX)

    probCrossVect = [0.7,0.75,0.8,0.85,0.9,0.95]
    k_wayTournamentVect = [0.2,0.3,0.4,0.5]
    casesTestCase1Dim2 = TrabCases()

    casesTestCase2Dim2 = TrabCases()
    for i in range(len(probCrossVect)):
        for j in range(len(k_wayTournamentVect)):
            casesTestCase1Dim2.testCaseTournament(problem_dict=PROBLEM_DICT_NCONVEX,pc=probCrossVect[i],k_way=k_wayTournamentVect[j])
            casesTestCase2Dim2.testCaseTournament(problem_dict=PROBLEM_DICT_NCONVEX,pc=probCrossVect[i],k_way=k_wayTournamentVect[j])
    casesTestCase1Dim2.npArray()

    plot_heatmap_with_points_testCase(func=FUNC_CONVEX, cases=casesTestCase1Dim2,name = NAME_CONVEX)
    plot_heatmap_with_points_testCase(func=FUNC_NCONVEX, cases=casesTestCase2Dim2,name = NAME_NCONVEX)

if __name__ == "__main__":
    run_test_cases()
