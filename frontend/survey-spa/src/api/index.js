import axios from 'axios'

const API_URL = process.env.API_URL

export function fetchSurveys() {
    return axios.get(`${API_URL}/surveys/`)
}

export function fetchSurvey(surveyId) {
    return axios.get(`${API_URL}/surveys/${surveyId}/`)
}

export function saveSurveyResponse(surveyResponse) {
    return axios.put(`${API_URL}/surveys/${surveyResponse.id}/`, surveyResponse)
}

export function postNewSurvey(survey, jwt) {
    return axios.post(`${API_URL}/surveys/`, survey, {
        headers: { Authorization: `Bearer ${jwt}` },
    })
}

export function authenticate(userData) {
    return axios.post(`${API_URL}/login/`, userData)
}

export function register(userData) {
    return axios.post(`${API_URL}/register/`, userData)
}
