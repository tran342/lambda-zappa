<template>
  <div>
    <div>
      <span>Please select Risk Type: </span>
      <select v-model="selectedRiskTypeId" v-on="changeRiskType(selectedRiskTypeId)">
        <option disabled selected value="">Please select</option>
        <option v-for="riskType in riskTypes" v-bind:value="riskType.id" v-bind:key="riskType.id">{{ riskType.name }}</option>
      </select>
    </div>
    <div v-if="selectedRiskTypeId !== ''">
      <div class="form-style">
        <form>
          <fieldset>
            <legend>{{ selectedRiskType.name }}</legend>
            <div v-for="f in selectedRiskType.fields" v-bind:key="f.id">
              <label>{{ f.name }} <span v-if="f.is_required">*</span>:</label>
              <label class="desc"><i>{{ f.description }}</i></label>
              <text-comp v-if="f.field_type === 'text'"></text-comp>
              <number-comp v-if="f.field_type === 'number'"></number-comp>
              <date-comp v-if="f.field_type === 'date'"></date-comp>
              <select-comp v-if="f.field_type === 'enum'" v-bind:data="f.read_enum_values"></select-comp>
            </div>
          </fieldset>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import TextComp from './TextComp.vue'
import NumberComp from './NumberComp.vue'
import DateComp from './DateComp.vue'
import SelectComp from './SelectComp.vue'

export default {
  components: {
    SelectComp,
    DateComp,
    NumberComp,
    'text-comp': TextComp,
    'number-comp': NumberComp,
    'date-comp': DateComp,
    'select-comp': SelectComp
  },
  data () {
    return {
      selectedRiskTypeId: '',
      selectedRiskType: null
    }
  },
  computed: {
    ...mapGetters({
      riskTypes: 'getRiskTypes',
      riskType: 'getRiskTypeById'
    })
  },
  methods: {
    changeRiskType (event) {
      if (this.selectedRiskTypeId !== '') {
        this.selectedRiskType = this.riskType(parseInt(this.selectedRiskTypeId))
      }
    }
  },
  created () {
    this.$store.dispatch('requestRiskTypes')
  }
}
</script>

<style scoped>
  .form-style {
    max-width: 500px;
    margin: 10px auto;
    padding: 20px;
    background: #f4f7f8;
    border-radius: 8px;
    font-family: Georgia, "Times New Roman", Times, serif;
  }
  .form-style fieldset {
    border: none;
  }
  .form-style legend {
    font-size: 1.4em;
    margin-bottom: 10px;
  }
  .form-style label {
    display: block;
    margin-bottom: 8px;
  }
  .form-style input[type="text"],
  .form-style input[type="date"],
  .form-style input[type="datetime"],
  .form-style input[type="email"],
  .form-style input[type="number"],
  .form-style input[type="search"],
  .form-style input[type="time"],
  .form-style input[type="url"],
  .form-style textarea,
  .form-style select {
    font-family: Georgia, "Times New Roman", Times, serif;
    border: none;
    border-radius: 4px;
    font-size: 16px;
    margin: 0;
    outline: 0;
    padding: 7px;
    width: 100%;
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    background-color: #e8eeef;
    color:#8a97a0;
    -webkit-box-shadow: 0 1px 0 rgba(0,0,0,0.03) inset;
    box-shadow: 0 1px 0 rgba(0,0,0,0.03) inset;
    margin-bottom: 30px;
  }
  .form-style input[type="text"]:focus,
  .form-style input[type="date"]:focus,
  .form-style input[type="datetime"]:focus,
  .form-style input[type="email"]:focus,
  .form-style input[type="number"]:focus,
  .form-style input[type="search"]:focus,
  .form-style input[type="time"]:focus,
  .form-style input[type="url"]:focus,
  .form-style textarea:focus,
  .form-style select:focus{
    background: #d2d9dd;
  }
  .form-style select {
    -webkit-appearance: menulist-button;
    height:35px;
  }
  .form-style .desc {
    font-size: 10px;
    margin-left: 10px;
  }
</style>
