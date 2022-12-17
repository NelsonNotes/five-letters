import React, { useEffect } from 'react'

import './GamePage.css'

import { useAppDispatch } from '../../hooks/app'
import { sessionFlush } from '../../store/session/utils'
import { sessionOperations } from '../../store/session/operations'
import { userOperations } from '../../store/user/operations'
import { useSelector } from 'react-redux'
import { selectUser } from '../../store/user/selectors'
import { selectSession } from '../../store/session/selectors'

export const GamePage: React.FC = () => {
	const dispatch = useAppDispatch()

	const user = useSelector(selectUser)
	const session = useSelector(selectSession)

	const logoutHandler = () => {
		sessionFlush()
		dispatch(sessionOperations.clear())
	}

	useEffect(() => {
		if (session.data) dispatch(userOperations.fetch())
	}, [session])

	useEffect(() => {
		console.log('NELSON user', user)
	}, [user])

	return (
		<div>
			<div>This is a Game Page</div>
			<button onClick={logoutHandler}>Logout</button>
		</div>
	)
}
