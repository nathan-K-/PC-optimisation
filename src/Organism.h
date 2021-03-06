//
// Created by arrouan on 28/09/16.
//

#ifndef PDC_EVOL_MODEL_ORGANISM_H
#define PDC_EVOL_MODEL_ORGANISM_H


#include <vector>
#include <unordered_map>
#include <map>
#include "Move.h"
#include "Pump.h"
#include "Protein.h"
#include "RNA.h"
#include "Common.h"
#include "GridCell.h"

class DNA;

class Organism {
 public:
    Organism(Organism* organism);
    Organism(DNA* dna) { dna_ = dna;};
    ~Organism();

    DNA* dna_;
    std::vector<RNA*> rna_list_;
    std::vector<std::unordered_map<float,float>> rna_influence_; //from unordered map to vector
    std::vector<std::unordered_map<float,Protein*>> rna_produce_protein_; //from unordered map to vector

    std::vector<Protein*> protein_fitness_list_;
    std::vector<Protein*> protein_TF_list_;
    std::vector<Protein*> protein_poison_list_;
    std::vector<Protein*> protein_antipoison_list_;

    std::map<float,Protein*> protein_list_map_; //from unordered map to map (is it really better ?)

    std::vector<Pump*> pump_list_;
    std::vector<Move*> move_list_;

    float metabolic_error[Common::Metabolic_Error_Precision];
    float sum_metabolic_error;

    GridCell* gridcell_;

    float fitness_ = -1;

    int life_duration_=0;
    int move_success_=0;
    int dupli_success_=0;

    void init_organism();
    void translate_RNA();
    void translate_protein();
    void build_regulation_network();
    void translate_pump();
    void translate_move();

    void mutate();

    void activate_pump();
	void activate_pump_step1(Pump * & it);
	void activate_pump_step2(Pump * & it);
    bool dying_or_not();
    void compute_fitness();

	void compute_protein_concentration_step1();
	void compute_protein_concentration_step1dot5(float delta_pos, float delta_neg, int rna_id);
	std::unordered_map<float, float> compute_protein_concentration_step2();
	void compute_protein_concentration_step3(std::unordered_map<float, float>& delta_concentration);
    void compute_protein_concentration();

};

#endif //PDC_EVOL_MODEL_ORGANISM_H
