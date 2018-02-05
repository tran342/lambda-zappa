<template>
  <div>
    <div>
      <span>Please select Risk Type</span>
      <br>
      <select v-model="selectedRiskTypeId" v-on="changeRiskType(selectedRiskTypeId)">
        <option disabled value="">[Select]</option>
        <option v-for="riskType in riskTypes" v-bind:value="riskType.id" v-bind:key="riskType.id">{{ riskType.name }}</option>
      </select>
    </div>
    <div v-if="selectedRiskTypeId !== ''">
      <span>You selected Risk Type: {{ selectedRiskType.name }}</span>
      <table>
        <tr>
          <td>Name</td>
          <td>{{ selectedRiskType.name }}</td>
        </tr>
        <tr v-for="f in selectedRiskType.fields" v-bind:key="f.id">
          <td colspan="2">
            <table>
              <tr>
                <td>Name</td>
                <td>{{ f.name }}</td>
              </tr>
              <tr>
                <td>Description</td>
                <td>{{ f.description }}</td>
              </tr>
              <tr>
                <td>Field Type</td>
                <td>{{ f.field_type }}</td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'

export default {
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
