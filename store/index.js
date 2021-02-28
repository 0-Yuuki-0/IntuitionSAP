  
import userSidebarItems from './data/userSidebarItems';
import clinicSidebarItems from './data/clinicSidebarItems';

export const state = () => ({
    userSidebarItems, 
    clinicSidebarItems,
    loggedIn: false,
    token: '',
    user: {},
});

export const mutations = {
    setToken(state, token) {
        state.token = token;
        state.loggedIn = true;
    },
    updateUser(state, user) {
        state.user = user;
    },
    logout(state) {
        state.user = {}
        state.token = '',
        state.loggedIn = false;
    }
}

export const actions = {
    async getUser({ state, commit }) {
        this.$axios.get('/api/token/get_user')
            .then(res => {
                console.log(res.data);
                commit('updateUser', res.data[0])
            });
    },
    logout({commit, $route}) {
        commit('logout');
        $nuxt.$router.push('/auth/login')
    }
}