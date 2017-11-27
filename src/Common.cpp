//
// Created by arrouan on 28/09/16.
//

#include <stdint.h>
#include <random>
#include "Common.h"

float Common::matrix_binding_[BINDING_MATRIX_SIZE*BINDING_MATRIX_SIZE];

void Common::init_binding_matrix(uint32_t seed) {

  std::mt19937 float_gen_;
  float_gen_.seed(seed);
  std::uniform_real_distribution<float> dis_number(-1, 1);
  std::uniform_int_distribution<int> dis_percent(0,100);

  for (int i = 0; i < BINDING_MATRIX_SIZE; i++) {
    for (int j = 0; j < BINDING_MATRIX_SIZE; j++) {
      if (dis_percent(float_gen_) > BINDING_MATRIX_ZERO_PERCENT)
        matrix_binding_[i*BINDING_MATRIX_SIZE+j]=dis_number(float_gen_);
      else
        matrix_binding_[i*BINDING_MATRIX_SIZE+j]=0;
    }
  }

}

void Common::save_binding_matrix() {
}

void Common::load_binding_matrix() {
}
